from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodBacsDebit(Base):
    __tablename__ = "payment_method_bacs_debit"
    fingerprint = Column(
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    )
    last4 = Column(
        String, comment="Last four digits of the bank account number", nullable=True
    )
    sort_code = Column(
        String,
        comment="Sort code of the bank account. (e.g., `10-20-30`)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodBacsDebit(fingerprint={fingerprint!r}, last4={last4!r}, sort_code={sort_code!r}, id={id!r})".format(
            fingerprint=self.fingerprint,
            last4=self.last4,
            sort_code=self.sort_code,
            id=self.id,
        )


__all__ = ["payment_method_bacs_debit"]
