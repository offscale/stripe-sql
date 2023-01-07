from sqlalchemy import Column, Integer, String


class Subscriptions_Resource_Payment_Settings(Base):
    __tablename__ = "subscriptions_resource_payment_settings"
    payment_method_options = Column(
        subscriptions_resource_payment_method_options,
        comment="[[FK(subscriptions_resource_payment_method_options)]] Payment-method-specific configuration to provide to invoices created by the subscription",
        nullable=True,
    )
    payment_method_types = Column(
        ARRAY(String),
        comment="The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)",
        nullable=True,
    )
    save_default_payment_method = Column(
        String,
        comment="Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscriptions_Resource_Payment_Settings(payment_method_options={payment_method_options!r}, payment_method_types={payment_method_types!r}, save_default_payment_method={save_default_payment_method!r}, id={id!r})".format(
            payment_method_options=self.payment_method_options,
            payment_method_types=self.payment_method_types,
            save_default_payment_method=self.save_default_payment_method,
            id=self.id,
        )


__all__ = ["subscriptions_resource_payment_settings"]
