from sqlalchemy import Column, Identity, Integer, String

from . import Base


class IssuingTransactionTreasury(Base):
    __tablename__ = "issuing_transaction_treasury"
    received_credit = Column(
        String,
        comment="The Treasury [ReceivedCredit](https://stripe.com/docs/api/treasury/received_credits) representing this Issuing transaction if it is a refund",
        nullable=True,
    )
    received_debit = Column(
        String,
        comment="The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) representing this Issuing transaction if it is a capture",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingTransactionTreasury(received_credit={received_credit!r}, received_debit={received_debit!r}, id={id!r})".format(
            received_credit=self.received_credit,
            received_debit=self.received_debit,
            id=self.id,
        )


__all__ = ["issuing_transaction_treasury"]
