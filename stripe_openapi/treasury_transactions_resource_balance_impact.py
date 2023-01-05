from sqlalchemy import Column, Integer


class Treasury_Transactions_Resource_Balance_Impact(Base):
    """
    Change to a FinancialAccount's balance
    """

    __tablename__ = "treasury_transactions_resource_balance_impact"
    cash = Column(
        Integer, comment="The change made to funds the user can spend right now"
    )
    inbound_pending = Column(
        Integer,
        comment="The change made to funds that are not spendable yet, but will become available at a later time",
    )
    outbound_pending = Column(
        Integer,
        comment="The change made to funds in the account, but not spendable because they are being held for pending outbound flows",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Transactions_Resource_Balance_Impact(cash={cash!r}, inbound_pending={inbound_pending!r}, outbound_pending={outbound_pending!r}, id={id!r})".format(
            cash=self.cash,
            inbound_pending=self.inbound_pending,
            outbound_pending=self.outbound_pending,
            id=self.id,
        )


__all__ = ["treasury_transactions_resource_balance_impact"]
