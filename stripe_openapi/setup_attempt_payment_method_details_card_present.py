from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class SetupAttemptPaymentMethodDetailsCardPresent(Base):
    __tablename__ = "setup_attempt_payment_method_details_card_present"
    generated_card = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="The ID of the Card PaymentMethod which was generated by this SetupAttempt",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupAttemptPaymentMethodDetailsCardPresent(generated_card={generated_card!r}, id={id!r})".format(
            generated_card=self.generated_card, id=self.id
        )


__all__ = ["setup_attempt_payment_method_details_card_present"]
