from sqlalchemy import Column, Integer


class Portal_Features(Base):
    __tablename__ = "portal_features"
    customer_update = Column(PortalCustomerUpdate)
    invoice_history = Column(PortalInvoiceList)
    payment_method_update = Column(PortalPaymentMethodUpdate)
    subscription_cancel = Column(PortalSubscriptionCancel)
    subscription_pause = Column(PortalSubscriptionPause)
    subscription_update = Column(PortalSubscriptionUpdate)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Portal_Features(customer_update={customer_update!r}, invoice_history={invoice_history!r}, payment_method_update={payment_method_update!r}, subscription_cancel={subscription_cancel!r}, subscription_pause={subscription_pause!r}, subscription_update={subscription_update!r}, id={id!r})".format(
            customer_update=self.customer_update,
            invoice_history=self.invoice_history,
            payment_method_update=self.payment_method_update,
            subscription_cancel=self.subscription_cancel,
            subscription_pause=self.subscription_pause,
            subscription_update=self.subscription_update,
            id=self.id,
        )


__all__ = ["portal_features"]
