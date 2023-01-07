from sqlalchemy import Column, Integer, String


class Payment_Intent_Processing(Base):
    __tablename__ = "payment_intent_processing"
    card = Column(
        payment_intent_card_processing,
        ForeignKey("payment_intent_card_processing"),
        nullable=True,
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
            "Payment_Intent_Processing(card={card!r}, type={type!r}, id={id!r})".format(
                card=self.card, type=self.type, id=self.id
            )
        )


__all__ = ["payment_intent_processing"]
