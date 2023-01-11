from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String

from . import Base


class InvoicesPaymentSettings(Base):
    __tablename__ = "invoices_payment_settings"
    default_mandate = Column(
        String,
        comment="ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice's default_payment_method or default_source, if set",
        nullable=True,
    )
    payment_method_options = Column(
        Integer,
        ForeignKey("invoices_payment_method_options.id"),
        comment="Payment-method-specific configuration to provide to the invoice’s PaymentIntent",
        nullable=True,
    )
    payment_method_types = Column(
        ARRAY(String),
        comment="The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicesPaymentSettings(default_mandate={default_mandate!r}, payment_method_options={payment_method_options!r}, payment_method_types={payment_method_types!r}, id={id!r})".format(
            default_mandate=self.default_mandate,
            payment_method_options=self.payment_method_options,
            payment_method_types=self.payment_method_types,
            id=self.id,
        )


__all__ = ["invoices_payment_settings"]
