from sqlalchemy import Column, String, Table

from . import metadata

FundingInstructionsBankTransferSpeiRecordJson = Table(
    "funding_instructions_bank_transfer_spei_recordjson",
    metadata,
    Column("bank_code", String, comment="The three-digit bank code"),
    Column(
        "bank_name",
        String,
        comment="The short banking institution name",
        primary_key=True,
    ),
    Column("clabe", String, comment="The CLABE number"),
)
__all__ = ["funding_instructions_bank_transfer_spei_record.json"]
