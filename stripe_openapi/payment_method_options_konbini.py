from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodOptionsKonbiniJson = Table(
    "payment_method_options_konbinijson",
    metadata,
    Column(
        "confirmation_number",
        String,
        comment="An optional 10 to 11 digit numeric-only string determining the confirmation code at applicable convenience stores",
        nullable=True,
    ),
    Column(
        "expires_after_days",
        Integer,
        comment="The number of calendar days (between 1 and 60) after which Konbini payment instructions will expire. For example, if a PaymentIntent is confirmed with Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will expire on Wednesday 23:59:59 JST",
        nullable=True,
    ),
    Column(
        "expires_at",
        Integer,
        comment="The timestamp at which the Konbini payment instructions will expire. Only one of `expires_after_days` or `expires_at` may be set",
        nullable=True,
    ),
    Column(
        "product_description",
        String,
        comment="A product descriptor of up to 22 characters, which will appear to customers at the convenience store",
        nullable=True,
    ),
    Column(
        "setup_future_usage",
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_konbini.json"]
