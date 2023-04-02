from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

GelatoReportIdNumberOptionsJson = Table(
    "gelato_report_id_number_optionsjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_report_id_number_options.json"]
