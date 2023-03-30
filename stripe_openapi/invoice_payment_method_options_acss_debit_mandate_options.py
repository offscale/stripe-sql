from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsAcssDebitMandateOptions.Json = Table(
    "invoice_payment_method_options_acss_debit_mandate_options.json",
    metadata,
    Column(
        "transaction_type",
        String,
        comment="Transaction type of the mandate",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_acss_debit_mandate_options.json"]
