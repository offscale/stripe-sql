from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

GelatoDataIdNumberReportDate.Json = Table(
    "gelato_data_id_number_report_date.json",
    metadata,
    Column("day", Integer, comment="Numerical day between 1 and 31", nullable=True),
    Column("month", Integer, comment="Numerical month between 1 and 12", nullable=True),
    Column("year", Integer, comment="The four-digit year", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_data_id_number_report_date.json"]
