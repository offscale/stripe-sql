from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

FundingInstructionsBankTransferZenginRecord.Json = Table(
    "funding_instructions_bank_transfer_zengin_record.json",
    metadata,
    Column(
        "account_holder_name", String, comment="The account holder name", nullable=True
    ),
    Column("account_number", String, comment="The account number", nullable=True),
    Column(
        "account_type",
        String,
        comment="The bank account type. In Japan, this can only be `futsu` or `toza`",
        nullable=True,
    ),
    Column("bank_code", String, comment="The bank code of the account", nullable=True),
    Column("bank_name", String, comment="The bank name of the account", nullable=True),
    Column(
        "branch_code", String, comment="The branch code of the account", nullable=True
    ),
    Column(
        "branch_name", String, comment="The branch name of the account", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["funding_instructions_bank_transfer_zengin_record.json"]
