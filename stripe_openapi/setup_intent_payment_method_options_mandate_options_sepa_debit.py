from sqlalchemy import Column, Identity, Integer

from . import Base


class SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit(Base):
    __tablename__ = "setup_intent_payment_method_options_mandate_options_sepa_debit"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit(id={id!r})".format(
                id=self.id
            )
        )


__all__ = ["setup_intent_payment_method_options_mandate_options_sepa_debit"]
