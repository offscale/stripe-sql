from sqlalchemy import Column, String, Table

from . import metadata

FundingInstructionsBankTransferIbanRecordJson = Table(
    "funding_instructions_bank_transfer_iban_recordjson",
    metadata,
    Column(
        "account_holder_name",
        String,
        comment="The name of the person or business that owns the bank account",
        primary_key=True,
    ),
    Column("bic", String, comment="The BIC/SWIFT code of the account"),
    Column(
        "country",
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
    ),
    Column("iban", String, comment="The IBAN of the account"),
)
__all__ = ["funding_instructions_bank_transfer_iban_record.json"]
