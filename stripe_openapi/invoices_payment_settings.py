from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

InvoicesPaymentSettings.Json = Table(
    "invoices_payment_settings.json",
    metadata,
    Column(
        "default_mandate",
        String,
        comment="ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice's default_payment_method or default_source, if set",
        nullable=True,
    ),
    Column(
        "payment_method_options",
        InvoicesPaymentMethodOptions,
        ForeignKey("InvoicesPaymentMethodOptions"),
        comment="Payment-method-specific configuration to provide to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "payment_method_types",
        ARRAY(String),
        comment="The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_payment_settings.json"]
