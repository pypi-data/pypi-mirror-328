import csv
import logging

import polars as pl
from parsomics_core.entities import ProteinAnnotationEntry, ProteinAnnotationFile
from parsomics_core.entities.workflow.source import (
    Source,
    SourceCreate,
    SourceTransactions,
)
from parsomics_core.plugin_utils import search_protein_by_name
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

ANNOTATION_TYPE = "EC_NUMBER"  # tirar da versão final
# FILE_KEY = 2


class CleanParser(BaseModel):
    file: ProteinAnnotationFile
    assembly_key: int
    tool_key: int

    def to_dataframe(self) -> pl.DataFrame:
        rows = []
        with open(self.file.path, mode="r") as infile:
            reader = csv.reader(infile)
            for row in reader:
                id_val = row[0]
                for data in row[1:]:
                    rows.append([id_val, data])

        with open(self.file.path, mode="w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

        df = pl.read_csv(
            self.file.path,
            has_header=False,
            infer_schema=False,
        )

        df = df.with_columns(
            df[:, 0]
            .str.strip_chars('"')
            .str.split(" ")
            # .str.strip_chars(" ")
            .list.first()
            .alias(df.columns[0])
        )

        df = df.with_columns(df[:, 1].str.strip_chars("EC:"))

        rows = []

        for row in df.iter_rows():
            id_val, data = row
            entries = data.split(",")
            for entry in entries:
                ec_number, score = entry.split("/")
                rows.append(
                    (
                        id_val,
                        ec_number,
                        score,
                        ANNOTATION_TYPE,
                    )
                )

        schema: dict[str, pl.PolarsDataType] = {
            "protein_name": pl.String,
            "accession": pl.String,
            "score": pl.Float64,
            "annotation_type": pl.String,
            #            "file_key": pl.Int32, #Revisar na versão final
        }

        df = pl.DataFrame(rows, schema=schema, orient="row")

        df.write_csv("resultado_parser.csv")  # Retirar da versão final

        return df

    #
    #    def _add_source_key_to_df(self, engine, df) -> pl.DataFrame:
    #        with Session(engine) as session:
    #            # First, add all sources that are already in the database (and,
    #            # thus, already have a primary key) to the dictionary that relates
    #            # source name to primary key
    #            sources_in_clean = session.exec(select(Source)).all()
    #            source_name_to_key = {
    #                source.name: source.key for source in sources_in_clean
    #            }
    #        # Then, iterate over the sources in the DataFrame and add them
    #        # to the database if they are not present in the source_name_to_key
    #        # dictionary. Add them to the dictionary once they have been added
    #        # to the database and have a primary key
    #        source_names_in_df = df.select(pl.col("source_name")).unique().to_series()
    #        for source_name in source_names_in_df:
    #            if source_name not in source_name_to_key:
    #                source_create_model = SourceCreate(
    #                    name=source_name,
    #                    tool_key=self.tool_key,
    #                )
    #                with Session(engine) as session:
    #                    source_key = (
    #                        SourceTransactions()
    #                        .create(
    #                            session,
    #                            source_create_model,
    #                        )
    #                        .key
    #                    )
    #                source_name_to_key[source_name] = source_key
    #
    #        # Finally, use source_name_to_key to add source_key to the DataFrame
    #        df = df.with_columns(
    #            source_key=pl.col("source_name").replace(
    #                source_name_to_key,
    #                default=None,
    #            )
    #        )
    #
    #        # Drop source_name since we can get the Source object with source_key
    #        df = df.drop("source_name")
    #
    #        return df
    #
    def _add_file_key_to_df(self, df):
        return df.with_columns(pl.lit(self.file.key).alias("file_key"))

    #
    #    def _add_annotation_type_to_mappings(self, mappings):
    #        for mapping in mappings:
    #            mapping["annotation_type"] = CleanAnnotationType(mapping["annotation_type"])

    def _add_protein_key_to_mappings(self, mappings):
        protein_name_to_key = {}
        for mapping in mappings:
            protein_name = mapping["protein_name"]
            if protein_name not in protein_name_to_key:
                protein_key = search_protein_by_name(protein_name, self.assembly_key)
                protein_name_to_key[protein_name] = protein_key

            protein_key = protein_name_to_key[protein_name]
            mapping["protein_key"] = protein_key
            mapping.pop("protein_name")

    def _add_empty_details(self, mappings):
        # NOTE: Although the details field in ProteinAnnotation has a default
        # value of {} as per "Field(default={}, sa_column=Column(JSONB))", this
        # default value is not inserted when using bulk_insert_mappings, since
        # bulk_insert_mappings skips object construction
        #
        for mapping in mappings:
            mapping["details"] = {}

    def parse(self, engine) -> None:
        df = self.to_dataframe()
        #        df = self._add_source_key_to_df(engine, df)
        df = self._add_file_key_to_df(df)

        mappings = df.to_dicts()
        #        self._add_annotation_type_to_mappings(mappings) #deixar, mesmo que apareça automaticamente?
        self._add_protein_key_to_mappings(mappings)
        self._add_empty_details(mappings)

        #        for mapping in mappings: #Não deixar porque aqui annotation_type foi definido com a constante, deixar for abaixo?
        #        mapping["annotation_type"] = DbcanAnnotationType(mapping["annotation_type"])

        for mapping in mappings:
            mapping["annotation_type"] = ANNOTATION_TYPE

        #        for mapping in mappings:
        #            mapping["file_key"] = FILE_KEY

        with Session(engine) as session:
            try:
                session.bulk_insert_mappings(ProteinAnnotationEntry, mappings)
                session.commit()
                logging.info(
                    f"Added CLEAN entries from {self.file.path} to the database."
                )
            except IntegrityError as e:
                logging.warning(
                    f"Failed to add CLEAN entries from {self.file.path} to "
                    f"the database. Exception caught: {e}"
                )

        return mappings  # Tirar da versão final
