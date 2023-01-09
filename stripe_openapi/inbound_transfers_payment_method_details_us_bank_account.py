from sqlalchemy import Column, String

from . import Base


class InboundTransfersPaymentMethodDetailsUsBankAccount(Base):
    __tablename__ = "inbound_transfers_payment_method_details_us_bank_account"
    account_holder_type = Column(
        String, comment="Account holder type: individual or company", nullable=True
    )
    account_type = Column(
        String,
        comment="Account type: checkings or savings. Defaults to checking if omitted",
        nullable=True,
    )
    bank_name = Column(
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
        primary_key=True,
    )
    fingerprint = Column(
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    )
    last4 = Column(
        String, comment="Last four digits of the bank account number", nullable=True
    )
    network = Column(String, comment="The US bank account network used to debit funds")
    routing_number = Column(
        String, comment="Routing number of the bank account", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InboundTransfersPaymentMethodDetailsUsBankAccount(account_holder_type={account_holder_type!r}, account_type={account_type!r}, bank_name={bank_name!r}, fingerprint={fingerprint!r}, last4={last4!r}, network={network!r}, routing_number={routing_number!r})".format(
            account_holder_type=self.account_holder_type,
            account_type=self.account_type,
            bank_name=self.bank_name,
            fingerprint=self.fingerprint,
            last4=self.last4,
            network=self.network,
            routing_number=self.routing_number,
        )


__all__ = ["inbound_transfers_payment_method_details_us_bank_account"]
