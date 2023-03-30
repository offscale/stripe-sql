from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsBancontact.Json = Table(
    "invoice_payment_method_options_bancontact.json",
    metadata,
    Column(
        "preferred_language",
        String,
        comment="Preferred language of the Bancontact authorization page that the customer is redirected to",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_bancontact.json"]
