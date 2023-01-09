from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentIntentCardProcessing(Base):
    __tablename__ = "payment_intent_card_processing"
    customer_notification = Column(
        Integer,
        ForeignKey("payment_intent_processing_customer_notification.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentCardProcessing(customer_notification={customer_notification!r}, id={id!r})".format(
            customer_notification=self.customer_notification, id=self.id
        )


__all__ = ["payment_intent_card_processing"]
