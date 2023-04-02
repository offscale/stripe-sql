from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

FundingInstructionsBankTransferFinancialAddressJson = Table(
    "funding_instructions_bank_transfer_financial_addressjson",
    metadata,
    Column(
        "iban",
        FundingInstructionsBankTransferIbanRecord,
        ForeignKey("FundingInstructionsBankTransferIbanRecord"),
        nullable=True,
    ),
    Column(
        "sort_code",
        FundingInstructionsBankTransferSortCodeRecord,
        ForeignKey("FundingInstructionsBankTransferSortCodeRecord"),
        nullable=True,
    ),
    Column(
        "spei",
        FundingInstructionsBankTransferSpeiRecord,
        ForeignKey("FundingInstructionsBankTransferSpeiRecord"),
        nullable=True,
    ),
    Column(
        "supported_networks",
        ARRAY(String),
        comment="The payment networks supported by this FinancialAddress",
        nullable=True,
    ),
    Column("type", String, comment="The type of financial address"),
    Column(
        "zengin",
        FundingInstructionsBankTransferZenginRecord,
        ForeignKey("FundingInstructionsBankTransferZenginRecord"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["funding_instructions_bank_transfer_financial_address.json"]
