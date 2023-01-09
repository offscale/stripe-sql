from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodAuBecsDebit(Base):
    __tablename__ = "payment_method_au_becs_debit"
    bsb_number = Column(
        String,
        comment="Six-digit number identifying bank and branch associated with this bank account",
        nullable=True,
    )
    fingerprint = Column(
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    )
    last4 = Column(
        String, comment="Last four digits of the bank account number", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodAuBecsDebit(bsb_number={bsb_number!r}, fingerprint={fingerprint!r}, last4={last4!r}, id={id!r})".format(
            bsb_number=self.bsb_number,
            fingerprint=self.fingerprint,
            last4=self.last4,
            id=self.id,
        )


__all__ = ["payment_method_au_becs_debit"]
