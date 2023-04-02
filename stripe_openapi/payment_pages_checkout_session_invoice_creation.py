from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionInvoiceCreationJson = Table(
    "payment_pages_checkout_session_invoice_creationjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates whether invoice creation is enabled for the Checkout Session",
    ),
    Column(
        "invoice_data",
        PaymentPagesCheckoutSessionInvoiceSettings,
        ForeignKey("PaymentPagesCheckoutSessionInvoiceSettings"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_invoice_creation.json"]
