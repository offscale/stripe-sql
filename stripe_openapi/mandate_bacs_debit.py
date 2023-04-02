from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

MandateBacsDebitJson = Table(
    "mandate_bacs_debitjson",
    metadata,
    Column(
        "network_status",
        String,
        comment="The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`",
    ),
    Column(
        "reference",
        String,
        comment="The unique reference identifying the mandate on the Bacs network",
    ),
    Column(
        "url",
        String,
        comment="The URL that will contain the mandate that the customer has signed",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_bacs_debit.json"]
