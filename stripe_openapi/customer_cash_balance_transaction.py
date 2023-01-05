from sqlalchemy import Boolean, Column, Integer, String


class Customer_Cash_Balance_Transaction(Base):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid

    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.

    """

    __tablename__ = "customer_cash_balance_transaction"
    applied_to_payment = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction,
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    customer = Column(
        Customer,
        comment="The customer whose available cash balance changed as a result of this transaction",
    )
    ending_balance = Column(
        Integer,
        comment="The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    )
    funded = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction,
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    net_amount = Column(
        Integer,
        comment="The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    refunded_from_payment = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction,
        nullable=True,
    )
    type = Column(
        String,
        comment="The type of the cash balance transaction. One of `applied_to_payment`, `unapplied_from_payment`, `refunded_from_payment`, `funded`, `return_initiated`, or `return_canceled`. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types",
    )
    unapplied_from_payment = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction,
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Cash_Balance_Transaction(applied_to_payment={applied_to_payment!r}, created={created!r}, currency={currency!r}, customer={customer!r}, ending_balance={ending_balance!r}, funded={funded!r}, id={id!r}, livemode={livemode!r}, net_amount={net_amount!r}, object={object!r}, refunded_from_payment={refunded_from_payment!r}, type={type!r}, unapplied_from_payment={unapplied_from_payment!r})".format(
            applied_to_payment=self.applied_to_payment,
            created=self.created,
            currency=self.currency,
            customer=self.customer,
            ending_balance=self.ending_balance,
            funded=self.funded,
            id=self.id,
            livemode=self.livemode,
            net_amount=self.net_amount,
            object=self.object,
            refunded_from_payment=self.refunded_from_payment,
            type=self.type,
            unapplied_from_payment=self.unapplied_from_payment,
        )


__all__ = ["customer_cash_balance_transaction"]
