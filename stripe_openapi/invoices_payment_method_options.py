from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

InvoicesPaymentMethodOptions.Json = Table(
    "invoices_payment_method_options.json",
    metadata,
    Column(
        "acss_debit",
        InvoicePaymentMethodOptionsAcssDebit,
        ForeignKey("InvoicePaymentMethodOptionsAcssDebit"),
        comment="If paying by `acss_debit`, this sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "bancontact",
        InvoicePaymentMethodOptionsBancontact,
        ForeignKey("InvoicePaymentMethodOptionsBancontact"),
        comment="If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "card",
        InvoicePaymentMethodOptionsCard,
        ForeignKey("InvoicePaymentMethodOptionsCard"),
        comment="If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "customer_balance",
        InvoicePaymentMethodOptionsCustomerBalance,
        ForeignKey("InvoicePaymentMethodOptionsCustomerBalance"),
        comment="If paying by `customer_balance`, this sub-hash contains details about the Bank transfer payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "konbini",
        InvoicePaymentMethodOptionsKonbini,
        ForeignKey("InvoicePaymentMethodOptionsKonbini"),
        comment="If paying by `konbini`, this sub-hash contains details about the Konbini payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column(
        "us_bank_account",
        InvoicePaymentMethodOptionsUsBankAccount,
        ForeignKey("InvoicePaymentMethodOptionsUsBankAccount"),
        comment="If paying by `us_bank_account`, this sub-hash contains details about the ACH direct debit payment method options to pass to the invoice’s PaymentIntent",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_payment_method_options.json"]
