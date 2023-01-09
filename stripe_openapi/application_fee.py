from sqlalchemy import JSON, Boolean, Column, Integer, String

from stripe_openapi.balance_transaction import BalanceTransaction

from . import Base


class ApplicationFee(Base):
    __tablename__ = "application_fee"
    account = Column(
        Account,
        comment="[[FK(Account)]] ID of the Stripe account this fee was taken from",
    )
    amount = Column(Integer, comment="Amount earned, in %s")
    amount_refunded = Column(
        Integer,
        comment="Amount in %s refunded (can be less than the amount attribute on the fee if a partial refund was issued)",
    )
    application = Column(
        Application,
        comment="[[FK(Application)]] ID of the Connect application that earned the fee",
    )
    balance_transaction = Column(
        BalanceTransaction,
        comment="[[FK(BalanceTransaction)]] Balance transaction that describes the impact of this collected application fee on your account balance (not including refunds)",
        nullable=True,
    )
    charge = Column(
        Charge,
        comment="[[FK(Charge)]] ID of the charge that the application fee was taken from",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    originating_transaction = Column(
        Charge,
        comment="[[FK(Charge)]] ID of the corresponding charge on the platform account, if this fee was the result of a charge using the `destination` parameter",
        nullable=True,
    )
    refunded = Column(
        Boolean,
        comment="Whether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false",
    )
    refunds = Column(
        JSON, comment="A list of refunds that have been applied to the fee"
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ApplicationFee(account={account!r}, amount={amount!r}, amount_refunded={amount_refunded!r}, application={application!r}, balance_transaction={balance_transaction!r}, charge={charge!r}, created={created!r}, currency={currency!r}, id={id!r}, livemode={livemode!r}, object={object!r}, originating_transaction={originating_transaction!r}, refunded={refunded!r}, refunds={refunds!r})".format(
            account=self.account,
            amount=self.amount,
            amount_refunded=self.amount_refunded,
            application=self.application,
            balance_transaction=self.balance_transaction,
            charge=self.charge,
            created=self.created,
            currency=self.currency,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            originating_transaction=self.originating_transaction,
            refunded=self.refunded,
            refunds=self.refunds,
        )


__all__ = ["application_fee"]
