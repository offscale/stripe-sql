from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class PaymentIntentProcessing(Base):
    __tablename__ = "payment_intent_processing"
    card = Column(
        Integer, ForeignKey("payment_intent_card_processing.id"), nullable=True
    )
    type = Column(
        String,
        comment="Type of the payment method for which payment is in `processing` state, one of `card`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "PaymentIntentProcessing(card={card!r}, type={type!r}, id={id!r})".format(
                card=self.card, type=self.type, id=self.id
            )
        )


__all__ = ["payment_intent_processing"]
