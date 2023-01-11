from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class SubscriptionsResourcePaymentMethodOptions(Base):
    __tablename__ = "subscriptions_resource_payment_method_options"
    acss_debit = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_acss_debit.id"),
        comment="This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    bancontact = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_bancontact.id"),
        comment="This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    card = Column(
        Integer,
        ForeignKey("subscription_payment_method_options_card.id"),
        comment="This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    customer_balance = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_customer_balance.id"),
        comment="This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    konbini = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_konbini.id"),
        comment="This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription",
        nullable=True,
    )
    us_bank_account = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_us_bank_account.id"),
        comment="This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription",
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
