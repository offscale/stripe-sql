from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

InvoicePaymentMethodOptionsKonbini.Json = Table(
    "invoice_payment_method_options_konbini.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_konbini.json"]
