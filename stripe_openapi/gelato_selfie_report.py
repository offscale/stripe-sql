from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

GelatoSelfieReportJson = Table(
    "gelato_selfie_reportjson",
    metadata,
    Column(
        "document",
        String,
        comment="ID of the [File](https://stripe.com/docs/api/files) holding the image of the identity document used in this check",
        nullable=True,
    ),
    Column(
        "error",
        GelatoSelfieReportError,
        ForeignKey("GelatoSelfieReportError"),
        comment="Details on the verification error. Present when status is `unverified`",
        nullable=True,
    ),
    Column(
        "selfie",
        String,
        comment="ID of the [File](https://stripe.com/docs/api/files) holding the image of the selfie used in this check",
        nullable=True,
    ),
    Column("status", String, comment="Status of this `selfie` check"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_selfie_report.json"]
