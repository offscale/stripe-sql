from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentMethodOptionsCustomerBalanceBankTransfer.Json = Table(
    "payment_method_options_customer_balance_bank_transfer.json",
    metadata,
    Column(
        "eu_bank_transfer",
        PaymentMethodOptionsCustomerBalanceEuBankAccount,
        ForeignKey("PaymentMethodOptionsCustomerBalanceEuBankAccount"),
        nullable=True,
    ),
    Column(
        "requested_address_types",
        ARRAY(String),
        comment="List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.\n\nPermitted values include: `sort_code`, `zengin`, `iban`, or `spei`",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_customer_balance_bank_transfer.json"]
