from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions.Json = Table(
    "invoice_payment_method_options_us_bank_account_linked_account_options.json",
    metadata,
    Column(
        "permissions",
        ARRAY(String),
        comment="The list of permissions to request. The `payment_method` permission must be included",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_us_bank_account_linked_account_options.json"]
