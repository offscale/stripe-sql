from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

SubscriptionsResourcePaymentMethodOptions.Json = Table(
    "subscriptions_resource_payment_method_options.json",
    metadata,
    Column(
        "acss_debit",
        InvoicePaymentMethodOptionsAcssDebit,
        ForeignKey("InvoicePaymentMethodOptionsAcssDebit"),
        comment="This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "bancontact",
        InvoicePaymentMethodOptionsBancontact,
        ForeignKey("InvoicePaymentMethodOptionsBancontact"),
        comment="This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "card",
        SubscriptionPaymentMethodOptionsCard,
        ForeignKey("SubscriptionPaymentMethodOptionsCard"),
        comment="This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "customer_balance",
        InvoicePaymentMethodOptionsCustomerBalance,
        ForeignKey("InvoicePaymentMethodOptionsCustomerBalance"),
        comment="This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "konbini",
        InvoicePaymentMethodOptionsKonbini,
        ForeignKey("InvoicePaymentMethodOptionsKonbini"),
        comment="This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column(
        "us_bank_account",
        InvoicePaymentMethodOptionsUsBankAccount,
        ForeignKey("InvoicePaymentMethodOptionsUsBankAccount"),
        comment="This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscriptions_resource_payment_method_options.json"]
