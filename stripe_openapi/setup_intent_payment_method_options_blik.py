from sqlalchemy import Column, Integer


class Setup_Intent_Payment_Method_Options_Blik(Base):
    __tablename__ = "setup_intent_payment_method_options_blik"
    mandate_options = Column(
        SetupIntentPaymentMethodOptionsMandateOptionsBlik, nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Intent_Payment_Method_Options_Blik(mandate_options={mandate_options!r}, id={id!r})".format(
            mandate_options=self.mandate_options, id=self.id
        )


__all__ = ["setup_intent_payment_method_options_blik"]
