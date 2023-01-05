from sqlalchemy import Boolean, Column, Integer, String


class Customer_Balance_Transaction(Base):
    """
    Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) value,

    which denotes a debit or credit that's automatically applied to their next invoice upon finalization.
    You may modify the value directly by using the [update customer API](https://stripe.com/docs/api/customers/update),
    or by creating a Customer Balance Transaction, which increments or decrements the customer's `balance` by the specified `amount`.

    Related guide: [Customer Balance](https://stripe.com/docs/billing/customer/balance) to learn more.

    """

    __tablename__ = "customer_balance_transaction"
    amount = Column(
        Integer,
        comment="The amount of the transaction. A negative value is a credit for the customer's balance, and a positive value is a debit to the customer's `balance`",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    credit_note = Column(
        CreditNote,
        comment="The ID of the credit note (if any) related to the transaction",
        nullable=True,
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    customer = Column(
        Customer, comment="The ID of the customer the transaction belongs to"
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    ending_balance = Column(
        Integer,
        comment="The customer's `balance` after the transaction was applied. A negative value decreases the amount due on the customer's next invoice. A positive value increases the amount due on the customer's next invoice",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice = Column(
        Invoice,
        comment="The ID of the invoice (if any) related to the transaction",
        nullable=True,
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    type = Column(
        String,
        comment="Transaction type: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `unspent_receiver_credit`, or `unapplied_from_invoice`. See the [Customer Balance page](https://stripe.com/docs/billing/customer/balance#types) to learn more about transaction types",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Balance_Transaction(amount={amount!r}, created={created!r}, credit_note={credit_note!r}, currency={currency!r}, customer={customer!r}, description={description!r}, ending_balance={ending_balance!r}, id={id!r}, invoice={invoice!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, type={type!r})".format(
            amount=self.amount,
            created=self.created,
            credit_note=self.credit_note,
            currency=self.currency,
            customer=self.customer,
            description=self.description,
            ending_balance=self.ending_balance,
            id=self.id,
            invoice=self.invoice,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            type=self.type,
        )


__all__ = ["customer_balance_transaction"]
