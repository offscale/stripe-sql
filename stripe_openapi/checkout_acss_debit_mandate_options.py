from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

CheckoutAcssDebitMandateOptions.Json = Table(
    "checkout_acss_debit_mandate_options.json",
    metadata,
    Column(
        "custom_mandate_url",
        String,
        comment="A URL for custom mandate text",
        nullable=True,
    ),
    Column(
        "default_for",
        ARRAY(String),
        comment="List of Stripe products where this mandate can be selected automatically. Returned when the Session is in `setup` mode",
        nullable=True,
    ),
    Column(
        "interval_description",
        String,
        comment="Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'",
        nullable=True,
    ),
    Column(
        "payment_schedule",
        String,
        comment="Payment schedule for the mandate",
        nullable=True,
    ),
    Column(
        "transaction_type",
        String,
        comment="Transaction type of the mandate",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["checkout_acss_debit_mandate_options.json"]
