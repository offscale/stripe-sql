from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

MandateUsBankAccount.Json = Table(
    "mandate_us_bank_account.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_us_bank_account.json"]
