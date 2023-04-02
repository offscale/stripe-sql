from sqlalchemy import Column, Identity, Integer, String, Table, list

from . import metadata

FundingInstructionsBankTransferJson = Table(
    "funding_instructions_bank_transferjson",
    metadata,
    Column("country", String, comment="The country of the bank account to fund"),
    Column(
        "financial_addresses",
        list,
        comment="A list of financial addresses that can be used to fund a particular balance",
    ),
    Column("type", String, comment="The bank_transfer type"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["funding_instructions_bank_transfer.json"]
