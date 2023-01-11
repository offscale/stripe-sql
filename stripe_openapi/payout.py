from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class Payout(Base):
    """
    A `Payout` object is created when you receive funds from Stripe, or when you

    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    as well as list all payouts. Payouts are made on [varying
    schedules](/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving Payouts](https://stripe.com/docs/payouts).

    """

    __tablename__ = "payout"
    amount = Column(
        Integer,
        comment="Amount (in %s) to be transferred to your bank account or debit card",
    )
    arrival_date = Column(
        Integer,
        comment="Date the payout is expected to arrive in the bank. This factors in delays like weekends or bank holidays",
    )
    automatic = Column(
        Boolean,
        comment="Returns `true` if the payout was created by an [automated payout schedule](https://stripe.com/docs/payouts#payout-schedule), and `false` if it was [requested manually](https://stripe.com/docs/payouts#manual-payouts)",
    )
    balance_transaction = Column(
        String,
        ForeignKey("balance_transaction.id"),
        comment="ID of the balance transaction that describes the impact of this payout on your account balance",
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
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    destination = Column(
        Integer,
        ForeignKey("external_account.id"),
        comment="ID of the bank account or card the payout was sent to",
        nullable=True,
    )
    failure_balance_transaction = Column(
        String,
        ForeignKey("balance_transaction.id"),
        comment="If the payout failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance",
        nullable=True,
    )
    failure_code = Column(
        String,
        comment="Error code explaining reason for payout failure if available. See [Types of payout failures](https://stripe.com/docs/api#payout_failures) for a list of failure codes",
        nullable=True,
    )
    failure_message = Column(
        String,
        comment="Message to user further explaining reason for payout failure if available",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    method = Column(
        String,
        comment="The method used to send this payout, which can be `standard` or `instant`. `instant` is only supported for payouts to debit cards. (See [Instant payouts for marketplaces](https://stripe.com/blog/instant-payouts-for-marketplaces) for more information.)",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    original_payout = Column(
        Payout,
        ForeignKey("Payout"),
        comment="If the payout reverses another, this is the ID of the original payout",
        nullable=True,
    )
    reversed_by = Column(
        Payout,
        ForeignKey("Payout"),
        comment="If the payout was reversed, this is the ID of the payout that reverses this payout",
        nullable=True,
    )
    source_type = Column(
        String,
        comment="The source balance this payout came from. One of `card`, `fpx`, or `bank_account`",
    )
    statement_descriptor = Column(
        String,
        comment="Extra information about a payout to be displayed on the user's bank statement",
        nullable=True,
    )
    status = Column(
        String,
        comment="Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it is submitted to the bank, when it becomes `in_transit`. The status then changes to `paid` if the transaction goes through, or to `failed` or `canceled` (within 5 business days). Some failed payouts may initially show as `paid` but then change to `failed`",
    )
    type = Column(String, comment="Can be `bank_account` or `card`")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payout(amount={amount!r}, arrival_date={arrival_date!r}, automatic={automatic!r}, balance_transaction={balance_transaction!r}, created={created!r}, currency={currency!r}, description={description!r}, destination={destination!r}, failure_balance_transaction={failure_balance_transaction!r}, failure_code={failure_code!r}, failure_message={failure_message!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, method={method!r}, object={object!r}, original_payout={original_payout!r}, reversed_by={reversed_by!r}, source_type={source_type!r}, statement_descriptor={statement_descriptor!r}, status={status!r}, type={type!r})".format(
            amount=self.amount,
            arrival_date=self.arrival_date,
            automatic=self.automatic,
            balance_transaction=self.balance_transaction,
            created=self.created,
            currency=self.currency,
            description=self.description,
            destination=self.destination,
            failure_balance_transaction=self.failure_balance_transaction,
            failure_code=self.failure_code,
            failure_message=self.failure_message,
            id=self.id,
            livemode=self.livemode,
            metadata=self.metadata,
            method=self.method,
            object=self.object,
            original_payout=self.original_payout,
            reversed_by=self.reversed_by,
            source_type=self.source_type,
            statement_descriptor=self.statement_descriptor,
            status=self.status,
            type=self.type,
        )


__all__ = ["payout"]
