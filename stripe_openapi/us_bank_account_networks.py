from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

UsBankAccountNetworks.Json = Table(
    "us_bank_account_networks.json",
    metadata,
    Column("preferred", String, comment="The preferred network", nullable=True),
    Column("supported", ARRAY(String), comment="All supported networks"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["us_bank_account_networks.json"]
