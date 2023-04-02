from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

InvoicePaymentMethodOptionsKonbiniJson = Table(
    "invoice_payment_method_options_konbinijson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_konbini.json"]
