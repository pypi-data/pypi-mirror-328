from collections.abc import Sequence
from dataclasses import dataclass

import google.cloud.bigquery as bq

from ._types import LatLon
from .auth import SecretSet


@dataclass
class BigQueryTable(SecretSet):
    GOOGLE_PROJECT_ID: str
    GOOGLE_DATASET_ID: str
    GOOGLE_TABLE_ID: str

    # _ <- tells SecretSet to ignore this field
    _bq_client: bq.Client

    @property
    def full_table_id(self) -> str:
        return f"{self.GOOGLE_PROJECT_ID.lower()}.{self.GOOGLE_DATASET_ID.lower()}.{self.GOOGLE_TABLE_ID.lower()}"

    @property
    def table(self) -> bq.Table:
        table_ref = self._bq_client.dataset(self.GOOGLE_DATASET_ID).table(
            self.GOOGLE_TABLE_ID
        )
        table = self._bq_client.get_table(table_ref)
        return table

    @property
    def schema(self) -> list[bq.SchemaField]:
        return self.table.schema  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]

    def modify_schema(self, new_schema: list[bq.SchemaField]) -> None:
        self.table.schema = new_schema
        _ = self._bq_client.update_table(self.table, ["schema"])

    @property
    def bq_client(self):
        return self._bq_client


@dataclass
class GeoSpatialJoinArgs:
    coords: Sequence[LatLon]
    geo_lookup_table: BigQueryTable
    lat_column: str = "lat"
    lon_column: str = "lon"
    new_coords_point_alias: str = "new_coords"
    new_coords_cte_name: str = "new_lon_lats"
    geo_lookup_table_point_alias: str = (
        "lonlat_geo"  # alias to combine lat and lon column
    )
    geo_lookup_table_cte_name: str = "lookup_coords"
    country_column: str = "country"
    city_column: str = "city"
    state_column: str = "state"
