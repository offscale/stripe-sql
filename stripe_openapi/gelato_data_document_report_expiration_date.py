from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

GelatoDataDocumentReportExpirationDateJson = Table(
    "gelato_data_document_report_expiration_datejson",
    metadata,
    Column("day", Integer, comment="Numerical day between 1 and 31", nullable=True),
    Column("month", Integer, comment="Numerical month between 1 and 12", nullable=True),
    Column("year", Integer, comment="The four-digit year", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_data_document_report_expiration_date.json"]
