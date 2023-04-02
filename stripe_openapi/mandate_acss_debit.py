from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

MandateAcssDebitJson = Table(
    "mandate_acss_debitjson",
    metadata,
    Column(
        "default_for",
        ARRAY(String),
        comment="List of Stripe products where this mandate can be selected automatically",
        nullable=True,
    ),
    Column(
        "interval_description",
        String,
        comment="Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'",
        nullable=True,
    ),
    Column("payment_schedule", String, comment="Payment schedule for the mandate"),
    Column("transaction_type", String, comment="Transaction type of the mandate"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_acss_debit.json"]
