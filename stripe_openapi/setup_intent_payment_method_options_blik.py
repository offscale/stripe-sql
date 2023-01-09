from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class SetupIntentPaymentMethodOptionsBlik(Base):
    __tablename__ = "setup_intent_payment_method_options_blik"
    mandate_options = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_mandate_options_blik.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentPaymentMethodOptionsBlik(mandate_options={mandate_options!r}, id={id!r})".format(
            mandate_options=self.mandate_options, id=self.id
        )


__all__ = ["setup_intent_payment_method_options_blik"]
