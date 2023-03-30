from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SubscriptionsResourcePaymentSettings.Json = Table(
    "subscriptions_resource_payment_settings.json",
    metadata,
    Column(
        "payment_method_options",
        SubscriptionsResourcePaymentMethodOptions,
        ForeignKey("SubscriptionsResourcePaymentMethodOptions"),
        comment="Payment-method-specific configuration to provide to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "payment_method_types",
        ARRAY(String),
        comment="The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)",
        nullable=True,
    ),
    Column(
        "save_default_payment_method",
        String,
        comment="Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscriptions_resource_payment_settings.json"]
