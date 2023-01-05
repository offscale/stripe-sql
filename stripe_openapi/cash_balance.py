from sqlalchemy import Boolean, Column, Integer, String


class Cash_Balance(Base):
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    __tablename__ = "cash_balance"
    available = Column(
        JSON,
        comment="A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    )
    customer = Column(
        String,
        comment="The ID of the customer whose cash balance this object represents",
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    settings = Column(CustomerBalanceCustomerBalanceSettings)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Cash_Balance(available={available!r}, customer={customer!r}, livemode={livemode!r}, object={object!r}, settings={settings!r}, id={id!r})".format(
            available=self.available,
            customer=self.customer,
            livemode=self.livemode,
            object=self.object,
            settings=self.settings,
            id=self.id,
        )


__all__ = ["cash_balance"]
