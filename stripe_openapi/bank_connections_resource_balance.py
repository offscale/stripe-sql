from sqlalchemy import Column, Integer, String


class Bank_Connections_Resource_Balance(Base):
    __tablename__ = "bank_connections_resource_balance"
    as_of = Column(
        Integer,
        comment="The time that the external institution calculated this balance. Measured in seconds since the Unix epoch",
    )
    cash = Column(
        bank_connections_resource_balance_api_resource_cash_balance,
        ForeignKey("bank_connections_resource_balance_api_resource_cash_balance"),
        nullable=True,
    )
    credit = Column(
        bank_connections_resource_balance_api_resource_credit_balance,
        ForeignKey("bank_connections_resource_balance_api_resource_credit_balance"),
        nullable=True,
    )
    current = Column(
        JSON,
        comment="The balances owed to (or by) the account holder.\n\nEach key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.\n\nEach value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder",
    )
    type = Column(
        String,
        comment="The `type` of the balance. An additional hash is included on the balance with a name matching this value",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Bank_Connections_Resource_Balance(as_of={as_of!r}, cash={cash!r}, credit={credit!r}, current={current!r}, type={type!r}, id={id!r})".format(
            as_of=self.as_of,
            cash=self.cash,
            credit=self.credit,
            current=self.current,
            type=self.type,
            id=self.id,
        )


__all__ = ["bank_connections_resource_balance"]
