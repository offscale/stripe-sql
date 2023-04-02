from sqlalchemy import Column, String, Table

from . import metadata

FundingInstructionsBankTransferSortCodeRecordJson = Table(
    "funding_instructions_bank_transfer_sort_code_recordjson",
    metadata,
    Column(
        "account_holder_name",
        String,
        comment="The name of the person or business that owns the bank account",
        primary_key=True,
    ),
    Column("account_number", String, comment="The account number"),
    Column("sort_code", String, comment="The six-digit sort code"),
)
__all__ = ["funding_instructions_bank_transfer_sort_code_record.json"]
