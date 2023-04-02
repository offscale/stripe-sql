from sqlalchemy import Column, String, Table

from . import metadata

TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccountJson = Table(
    "treasury_shared_resource_initiating_payment_method_details_us_bank_accountjson",
    metadata,
    Column("bank_name", String, comment="Bank name", nullable=True, primary_key=True),
    Column(
        "last4",
        String,
        comment="The last four digits of the bank account number",
        nullable=True,
    ),
    Column(
        "routing_number",
        String,
        comment="The routing number for the bank account",
        nullable=True,
    ),
)
__all__ = [
    "treasury_shared_resource_initiating_payment_method_details_us_bank_account.json"
]
