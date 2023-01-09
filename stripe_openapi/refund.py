from sqlalchemy import JSON, Column, ForeignKey, Integer, String

from stripe_openapi.balance_transaction import BalanceTransaction
from stripe_openapi.payment_intent import PaymentIntent
from stripe_openapi.transfer_reversal import TransferReversal

from . import Base


class Refund(Base):
    """
    `Refund` objects allow you to refund a charge that has previously been created

    but not yet refunded. Funds will be refunded to the credit or debit card that
    was originally charged.

    Related guide: [Refunds](https://stripe.com/docs/refunds).

    """

    __tablename__ = "refund"
    amount = Column(Integer, comment="Amount, in %s")
    balance_transaction = Column(
        BalanceTransaction,
        comment="[[FK(BalanceTransaction)]] Balance transaction that describes the impact on your account balance",
        nullable=True,
    )
    charge = Column(
        Charge,
        comment="[[FK(Charge)]] ID of the charge that was refunded",
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
        comment="An arbitrary string attached to the object. Often useful for displaying to users. (Available on non-card refunds only)",
        nullable=True,
    )
    failure_balance_transaction = Column(
        BalanceTransaction,
        comment="[[FK(BalanceTransaction)]] If the refund failed, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction",
        nullable=True,
    )
    failure_reason = Column(
        String,
        comment="If the refund failed, the reason for refund failure if known. Possible values are `lost_or_stolen_card`, `expired_or_canceled_card`, or `unknown`",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    instructions_email = Column(
        String,
        comment="Email to which refund instructions, if required, are sent to",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    next_action = Column(Integer, ForeignKey("refund_next_action.id"), nullable=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    payment_intent = Column(
        PaymentIntent,
        comment="[[FK(PaymentIntent)]] ID of the PaymentIntent that was refunded",
        nullable=True,
    )
    reason = Column(
        String,
        comment="Reason for the refund, either user-provided (`duplicate`, `fraudulent`, or `requested_by_customer`) or generated by Stripe internally (`expired_uncaptured_charge`)",
        nullable=True,
    )
    receipt_number = Column(
        String,
        comment="This is the transaction number that appears on email receipts sent for this refund",
        nullable=True,
    )
    source_transfer_reversal = Column(
        TransferReversal,
        comment="[[FK(TransferReversal)]] The transfer reversal that is associated with the refund. Only present if the charge came from another Stripe account. See the Connect documentation for details",
        nullable=True,
    )
    status = Column(
        String,
        comment="Status of the refund. For credit card refunds, this can be `pending`, `succeeded`, or `failed`. For other types of refunds, it can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Refer to our [refunds](https://stripe.com/docs/refunds#failed-refunds) documentation for more details",
        nullable=True,
    )
    transfer_reversal = Column(
        TransferReversal,
        comment="[[FK(TransferReversal)]] If the accompanying transfer was reversed, the transfer reversal object. Only applicable if the charge was created using the destination parameter",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Refund(amount={amount!r}, balance_transaction={balance_transaction!r}, charge={charge!r}, created={created!r}, currency={currency!r}, description={description!r}, failure_balance_transaction={failure_balance_transaction!r}, failure_reason={failure_reason!r}, id={id!r}, instructions_email={instructions_email!r}, metadata={metadata!r}, next_action={next_action!r}, object={object!r}, payment_intent={payment_intent!r}, reason={reason!r}, receipt_number={receipt_number!r}, source_transfer_reversal={source_transfer_reversal!r}, status={status!r}, transfer_reversal={transfer_reversal!r})".format(
            amount=self.amount,
            balance_transaction=self.balance_transaction,
            charge=self.charge,
            created=self.created,
            currency=self.currency,
            description=self.description,
            failure_balance_transaction=self.failure_balance_transaction,
            failure_reason=self.failure_reason,
            id=self.id,
            instructions_email=self.instructions_email,
            metadata=self.metadata,
            next_action=self.next_action,
            object=self.object,
            payment_intent=self.payment_intent,
            reason=self.reason,
            receipt_number=self.receipt_number,
            source_transfer_reversal=self.source_transfer_reversal,
            status=self.status,
            transfer_reversal=self.transfer_reversal,
        )


__all__ = ["refund"]
