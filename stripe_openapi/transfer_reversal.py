from sqlalchemy import JSON, Column, Integer, String

from stripe_openapi.balance_transaction import BalanceTransaction

from . import Base


class TransferReversal(Base):
    """
    [Stripe Connect](https://stripe.com/docs/connect) platforms can reverse transfers made to a

    connected account, either entirely or partially, and can also specify whether
    to refund any related application fees. Transfer reversals add to the
    platform's balance and subtract from the destination account's balance.

    Reversing a transfer that was made for a [destination
    charge](/docs/connect/destination-charges) is allowed only up to the amount of
    the charge. It is possible to reverse a
    [transfer_group](https://stripe.com/docs/connect/charges-transfers#transfer-options)
    transfer only if the destination account has enough balance to cover the
    reversal.

    Related guide: [Reversing Transfers](https://stripe.com/docs/connect/charges-transfers#reversing-transfers).

    """

    __tablename__ = "transfer_reversal"
    amount = Column(Integer, comment="Amount, in %s")
    balance_transaction = Column(
        BalanceTransaction,
        comment="[[FK(BalanceTransaction)]] Balance transaction that describes the impact on your account balance",
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
    destination_payment_refund = Column(
        Refund,
        comment="[[FK(Refund)]] Linked payment refund for the transfer reversal",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    source_refund = Column(
        Refund,
        comment="[[FK(Refund)]] ID of the refund responsible for the transfer reversal",
        nullable=True,
    )
    transfer = Column(
        Transfer, comment="[[FK(Transfer)]] ID of the transfer that was reversed"
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TransferReversal(amount={amount!r}, balance_transaction={balance_transaction!r}, created={created!r}, currency={currency!r}, destination_payment_refund={destination_payment_refund!r}, id={id!r}, metadata={metadata!r}, object={object!r}, source_refund={source_refund!r}, transfer={transfer!r})".format(
            amount=self.amount,
            balance_transaction=self.balance_transaction,
            created=self.created,
            currency=self.currency,
            destination_payment_refund=self.destination_payment_refund,
            id=self.id,
            metadata=self.metadata,
            object=self.object,
            source_refund=self.source_refund,
            transfer=self.transfer,
        )


__all__ = ["transfer_reversal"]
