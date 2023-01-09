from sqlalchemy import Column, Identity, Integer

from . import Base


class SetupAttemptPaymentMethodDetailsSepaDebit(Base):
    __tablename__ = "setup_attempt_payment_method_details_sepa_debit"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupAttemptPaymentMethodDetailsSepaDebit(id={id!r})".format(id=self.id)


__all__ = ["setup_attempt_payment_method_details_sepa_debit"]
