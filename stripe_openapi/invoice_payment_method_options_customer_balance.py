from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsCustomerBalanceJson = Table(
    "invoice_payment_method_options_customer_balancejson",
    metadata,
    Column(
        "bank_transfer",
        InvoicePaymentMethodOptionsCustomerBalanceBankTransfer,
        ForeignKey("InvoicePaymentMethodOptionsCustomerBalanceBankTransfer"),
        nullable=True,
    ),
    Column(
        "funding_type",
        String,
        comment="The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_customer_balance.json"]
