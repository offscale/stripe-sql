from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class IssuingAuthorizationTreasury(Base):
    __tablename__ = "issuing_authorization_treasury"
    received_credits = Column(
        ARRAY(String),
        comment="The array of [ReceivedCredits](https://stripe.com/docs/api/treasury/received_credits) associated with this authorization",
    )
    received_debits = Column(
        ARRAY(String),
        comment="The array of [ReceivedDebits](https://stripe.com/docs/api/treasury/received_debits) associated with this authorization",
    )
    transaction = Column(
        String,
        comment="The Treasury [Transaction](https://stripe.com/docs/api/treasury/transactions) associated with this authorization",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingAuthorizationTreasury(received_credits={received_credits!r}, received_debits={received_debits!r}, transaction={transaction!r}, id={id!r})".format(
            received_credits=self.received_credits,
            received_debits=self.received_debits,
            transaction=self.transaction,
            id=self.id,
        )


__all__ = ["issuing_authorization_treasury"]
