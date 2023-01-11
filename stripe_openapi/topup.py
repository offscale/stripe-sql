from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class Topup(Base):
    """
    To top up your Stripe balance, you create a top-up object. You can retrieve

    individual top-ups, as well as list all top-ups. Top-ups are identified by a
    unique, random ID.

    Related guide: [Topping Up your Platform Account](https://stripe.com/docs/connect/top-ups).

    """

    __tablename__ = "topup"
    amount = Column(Integer, comment="Amount transferred")
    balance_transaction = Column(
        String,
        ForeignKey("balance_transaction.id"),
        comment="ID of the balance transaction that describes the impact of this top-up on your account balance. May not be specified depending on status of top-up",
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
    expected_availability_date = Column(
        Integer,
        comment="Date the funds are expected to arrive in your Stripe account for payouts. This factors in delays like weekends or bank holidays. May not be specified depending on status of top-up",
        nullable=True,
    )
    failure_code = Column(
        String,
        comment="Error code explaining reason for top-up failure if available (see [the errors section](https://stripe.com/docs/api#errors) for a list of codes)",
        nullable=True,
    )
    failure_message = Column(
        String,
        comment="Message to user further explaining reason for top-up failure if available",
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
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    source = Column(
        Source,
        ForeignKey("Source"),
        comment="For most Stripe users, the source of every top-up is a bank account. This hash is then the [source object](https://stripe.com/docs/api#source_object) describing that bank account",
        nullable=True,
    )
    statement_descriptor = Column(
        String,
        comment="Extra information about a top-up. This will appear on your source's bank statement. It must contain at least one letter",
        nullable=True,
    )
    status = Column(
        String,
        comment="The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`, or `succeeded`",
    )
    transfer_group = Column(
        String,
        comment="A string that identifies this top-up as part of a group",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Topup(amount={amount!r}, balance_transaction={balance_transaction!r}, created={created!r}, currency={currency!r}, description={description!r}, expected_availability_date={expected_availability_date!r}, failure_code={failure_code!r}, failure_message={failure_message!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, source={source!r}, statement_descriptor={statement_descriptor!r}, status={status!r}, transfer_group={transfer_group!r})".format(
            amount=self.amount,
            balance_transaction=self.balance_transaction,
            created=self.created,
            currency=self.currency,
            description=self.description,
            expected_availability_date=self.expected_availability_date,
            failure_code=self.failure_code,
            failure_message=self.failure_message,
            id=self.id,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            source=self.source,
            statement_descriptor=self.statement_descriptor,
            status=self.status,
            transfer_group=self.transfer_group,
        )


__all__ = ["topup"]
