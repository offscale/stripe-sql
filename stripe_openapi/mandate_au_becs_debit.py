from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

MandateAuBecsDebit.Json = Table(
    "mandate_au_becs_debit.json",
    metadata,
    Column(
        "url",
        String,
        comment="The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_au_becs_debit.json"]
