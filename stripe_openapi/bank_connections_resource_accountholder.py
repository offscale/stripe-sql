from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.customer import Customer

from . import metadata

BankConnectionsResourceAccountholderJson = Table(
    "bank_connections_resource_accountholderjson",
    metadata,
    Column(
        "account",
        Account,
        ForeignKey("Account"),
        comment="The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`",
        nullable=True,
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("Customer"),
        comment="ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`",
        nullable=True,
    ),
    Column(
        "type", String, comment="Type of account holder that this account belongs to"
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_accountholder.json"]
