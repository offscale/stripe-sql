from sqlalchemy import Column, Identity, Integer

from . import Base


class CardMandatePaymentMethodDetails(Base):
    __tablename__ = "card_mandate_payment_method_details"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CardMandatePaymentMethodDetails(id={id!r})".format(id=self.id)


__all__ = ["card_mandate_payment_method_details"]
