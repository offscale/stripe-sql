from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

MandateSepaDebitJson = Table(
    "mandate_sepa_debitjson",
    metadata,
    Column("reference", String, comment="The unique reference of the mandate"),
    Column(
        "url",
        String,
        comment="The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_sepa_debit.json"]
