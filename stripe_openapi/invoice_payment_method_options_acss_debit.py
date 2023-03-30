from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsAcssDebit.Json = Table(
    "invoice_payment_method_options_acss_debit.json",
    metadata,
    Column(
        "mandate_options",
        InvoicePaymentMethodOptionsAcssDebitMandateOptions,
        ForeignKey("InvoicePaymentMethodOptionsAcssDebitMandateOptions"),
        nullable=True,
    ),
    Column(
        "verification_method",
        String,
        comment="Bank account verification method",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_acss_debit.json"]
