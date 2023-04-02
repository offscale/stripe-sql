from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

MandateSingleUseJson = Table(
    "mandate_single_usejson",
    metadata,
    Column(
        "amount", Integer, comment="On a single use mandate, the amount of the payment"
    ),
    Column(
        "currency",
        String,
        comment="On a single use mandate, the currency of the payment",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_single_use.json"]
