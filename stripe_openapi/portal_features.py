from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PortalFeatures(Base):
    __tablename__ = "portal_features"
    customer_update = Column(Integer, ForeignKey("portal_customer_update.id"))
    invoice_history = Column(Integer, ForeignKey("portal_invoice_list.id"))
    payment_method_update = Column(
        Integer, ForeignKey("portal_payment_method_update.id")
    )
    subscription_cancel = Column(Integer, ForeignKey("portal_subscription_cancel.id"))
    subscription_pause = Column(Integer, ForeignKey("portal_subscription_pause.id"))
    subscription_update = Column(Integer, ForeignKey("portal_subscription_update.id"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalFeatures(customer_update={customer_update!r}, invoice_history={invoice_history!r}, payment_method_update={payment_method_update!r}, subscription_cancel={subscription_cancel!r}, subscription_pause={subscription_pause!r}, subscription_update={subscription_update!r}, id={id!r})".format(
            customer_update=self.customer_update,
            invoice_history=self.invoice_history,
            payment_method_update=self.payment_method_update,
            subscription_cancel=self.subscription_cancel,
            subscription_pause=self.subscription_pause,
            subscription_update=self.subscription_update,
            id=self.id,
        )


__all__ = ["portal_features"]
