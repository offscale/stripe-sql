from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

GelatoSelfieReportError.Json = Table(
    "gelato_selfie_report_error.json",
    metadata,
    Column(
        "code",
        String,
        comment="A short machine-readable string giving the reason for the verification failure",
        nullable=True,
    ),
    Column(
        "reason",
        String,
        comment="A human-readable message giving the reason for the failure. These messages can be shown to your users",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_selfie_report_error.json"]
