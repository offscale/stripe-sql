from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

GelatoIdNumberReport.Json = Table(
    "gelato_id_number_report.json",
    metadata,
    Column(
        "dob",
        GelatoDataIdNumberReportDate,
        ForeignKey("GelatoDataIdNumberReportDate"),
        comment="Date of birth",
        nullable=True,
    ),
    Column(
        "error",
        GelatoIdNumberReportError,
        ForeignKey("GelatoIdNumberReportError"),
        comment="Details on the verification error. Present when status is `unverified`",
        nullable=True,
    ),
    Column("first_name", String, comment="First name", nullable=True),
    Column("id_number", String, comment="ID number", nullable=True),
    Column("id_number_type", String, comment="Type of ID number", nullable=True),
    Column("last_name", String, comment="Last name", nullable=True),
    Column("status", String, comment="Status of this `id_number` check"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_id_number_report.json"]
