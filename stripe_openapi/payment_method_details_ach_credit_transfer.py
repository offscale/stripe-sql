from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsAchCreditTransferJson = Table(
    "payment_method_details_ach_credit_transferjson",
    metadata,
    Column(
        "account_number",
        String,
        comment="Account number to transfer funds to",
        nullable=True,
    ),
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the routing number",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "routing_number",
        String,
        comment="Routing transit number for the bank account to transfer funds to",
        nullable=True,
    ),
    Column(
        "swift_code",
        String,
        comment="SWIFT code of the bank associated with the routing number",
        nullable=True,
    ),
)
__all__ = ["payment_method_details_ach_credit_transfer.json"]
