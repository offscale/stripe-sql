from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

GelatoReportIdNumberOptions.Json = Table(
    "gelato_report_id_number_options.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_report_id_number_options.json"]
