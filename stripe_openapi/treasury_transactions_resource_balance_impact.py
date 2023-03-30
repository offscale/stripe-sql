from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryTransactionsResourceBalanceImpact.Json = Table(
    "treasury_transactions_resource_balance_impact.json",
    metadata,
    Column(
        "cash", Integer, comment="The change made to funds the user can spend right now"
    ),
    Column(
        "inbound_pending",
        Integer,
        comment="The change made to funds that are not spendable yet, but will become available at a later time",
    ),
    Column(
        "outbound_pending",
        Integer,
        comment="The change made to funds in the account, but not spendable because they are being held for pending outbound flows",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_transactions_resource_balance_impact.json"]
