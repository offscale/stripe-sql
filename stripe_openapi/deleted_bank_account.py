from sqlalchemy import Boolean, Column, String, Table

from . import metadata

DeletedBankAccount.Json = Table(
    "deleted_bank_account.json",
    metadata,
    Column(
        "currency",
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account",
        nullable=True,
    ),
    Column("deleted", Boolean, comment="Always true for a deleted object"),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["deleted_bank_account.json"]
