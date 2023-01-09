from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class SetupIntentPaymentMethodOptionsUsBankAccount(Base):
    __tablename__ = "setup_intent_payment_method_options_us_bank_account"
    financial_connections = Column(
        Integer, ForeignKey("linked_account_options_us_bank_account.id"), nullable=True
    )
    verification_method = Column(
        String, comment="Bank account verification method", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentPaymentMethodOptionsUsBankAccount(financial_connections={financial_connections!r}, verification_method={verification_method!r}, id={id!r})".format(
            financial_connections=self.financial_connections,
            verification_method=self.verification_method,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options_us_bank_account"]
