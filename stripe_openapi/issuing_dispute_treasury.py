from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Treasury(Base):
    __tablename__ = "issuing_dispute_treasury"
    debit_reversal = Column(
        String,
        comment="The Treasury [DebitReversal](https://stripe.com/docs/api/treasury/debit_reversals) representing this Issuing dispute",
        nullable=True,
    )
    received_debit = Column(
        String,
        comment="The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) that is being disputed",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Treasury(debit_reversal={debit_reversal!r}, received_debit={received_debit!r}, id={id!r})".format(
            debit_reversal=self.debit_reversal,
            received_debit=self.received_debit,
            id=self.id,
        )


__all__ = ["issuing_dispute_treasury"]
