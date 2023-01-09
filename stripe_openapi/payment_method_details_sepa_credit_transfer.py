from sqlalchemy import Column, String

from . import Base


class PaymentMethodDetailsSepaCreditTransfer(Base):
    __tablename__ = "payment_method_details_sepa_credit_transfer"
    bank_name = Column(
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
        primary_key=True,
    )
    bic = Column(
        String,
        comment="Bank Identifier Code of the bank associated with the bank account",
        nullable=True,
    )
    iban = Column(
        String, comment="IBAN of the bank account to transfer funds to", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsSepaCreditTransfer(bank_name={bank_name!r}, bic={bic!r}, iban={iban!r})".format(
            bank_name=self.bank_name, bic=self.bic, iban=self.iban
        )


__all__ = ["payment_method_details_sepa_credit_transfer"]
