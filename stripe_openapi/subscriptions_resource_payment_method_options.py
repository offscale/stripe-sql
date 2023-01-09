from sqlalchemy import Column, Identity, Integer

from stripe_openapi.invoice_payment_method_options_acss_debit import (
    InvoicePaymentMethodOptionsAcssDebit,
)
from stripe_openapi.invoice_payment_method_options_bancontact import (
    InvoicePaymentMethodOptionsBancontact,
)
from stripe_openapi.invoice_payment_method_options_customer_balance import (
    InvoicePaymentMethodOptionsCustomerBalance,
)
from stripe_openapi.invoice_payment_method_options_konbini import (
    InvoicePaymentMethodOptionsKonbini,
)
from stripe_openapi.invoice_payment_method_options_us_bank_account import (
    InvoicePaymentMethodOptionsUsBankAccount,
)
from stripe_openapi.subscription_payment_method_options_card import (
    SubscriptionPaymentMethodOptionsCard,
)

from . import Base


class SubscriptionsResourcePaymentMethodOptions(Base):
    __tablename__ = "subscriptions_resource_payment_method_options"
    acss_debit = Column(
        InvoicePaymentMethodOptionsAcssDebit,
        comment="[[FK(InvoicePaymentMethodOptionsAcssDebit)]] This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    bancontact = Column(
        InvoicePaymentMethodOptionsBancontact,
        comment="[[FK(InvoicePaymentMethodOptionsBancontact)]] This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    card = Column(
        SubscriptionPaymentMethodOptionsCard,
        comment="[[FK(SubscriptionPaymentMethodOptionsCard)]] This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    customer_balance = Column(
        InvoicePaymentMethodOptionsCustomerBalance,
        comment="[[FK(InvoicePaymentMethodOptionsCustomerBalance)]] This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    konbini = Column(
        InvoicePaymentMethodOptionsKonbini,
        comment="[[FK(InvoicePaymentMethodOptionsKonbini)]] This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    us_bank_account = Column(
        InvoicePaymentMethodOptionsUsBankAccount,
        comment="[[FK(InvoicePaymentMethodOptionsUsBankAccount)]] This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionsResourcePaymentMethodOptions(acss_debit={acss_debit!r}, bancontact={bancontact!r}, card={card!r}, customer_balance={customer_balance!r}, konbini={konbini!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            bancontact=self.bancontact,
            card=self.card,
            customer_balance=self.customer_balance,
            konbini=self.konbini,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["subscriptions_resource_payment_method_options"]
