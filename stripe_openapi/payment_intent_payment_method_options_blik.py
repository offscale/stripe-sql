from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentIntentPaymentMethodOptionsBlik(Base):
    __tablename__ = "payment_intent_payment_method_options_blik"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentPaymentMethodOptionsBlik(id={id!r})".format(id=self.id)


__all__ = ["payment_intent_payment_method_options_blik"]
