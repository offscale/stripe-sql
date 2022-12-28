from sqlalchemy import Boolean, Column, Integer, String

class Transfer(Base):
    """
        A `Transfer` object is created when you move funds between Stripe accounts as
    
        part of Connect.
    
        Before April 6, 2017, transfers also represented movement of funds from a
        Stripe account to a card or bank account. This behavior has since been split
        out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
        information, read about the
        [transfer/payout split](https://stripe.com/docs/transfer-payout-split).
    
        Related guide: [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/charges-transfers).
    
        """
    __tablename__ = 'transfer'
    amount = Column(Integer, comment='Amount in %s to be transferred')
    amount_reversed = Column(Integer, comment='Amount in %s reversed (can be less than the amount attribute on the transfer if a partial reversal was issued)')
    balance_transaction = Column(BalanceTransaction, comment='Balance transaction that describes the impact of this transfer on your account balance', nullable=True)
    created = Column(Integer, comment='Time that this record of the transfer was first created')
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    description = Column(String, comment='An arbitrary string attached to the object. Often useful for displaying to users', nullable=True)
    destination = Column(Account, comment='ID of the Stripe account the transfer was sent to', nullable=True)
    destination_payment = Column(Charge, comment='If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer', nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format')
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    reversals = Column(JSON, comment='A list of reversals that have been applied to the transfer')
    reversed = Column(Boolean, comment='Whether the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false')
    source_transaction = Column(Charge, comment='ID of the charge or payment that was used to fund the transfer. If null, the transfer was funded from the available balance', nullable=True)
    source_type = Column(String, comment='The source balance this transfer came from. One of `card`, `fpx`, or `bank_account`', nullable=True)
    transfer_group = Column(String, comment='A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers#transfer-options) for details', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Transfer(amount={amount!r}, amount_reversed={amount_reversed!r}, balance_transaction={balance_transaction!r}, created={created!r}, currency={currency!r}, description={description!r}, destination={destination!r}, destination_payment={destination_payment!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, reversals={reversals!r}, reversed={reversed!r}, source_transaction={source_transaction!r}, source_type={source_type!r}, transfer_group={transfer_group!r})'.format(amount=self.amount, amount_reversed=self.amount_reversed, balance_transaction=self.balance_transaction, created=self.created, currency=self.currency, description=self.description, destination=self.destination, destination_payment=self.destination_payment, id=self.id, livemode=self.livemode, metadata=self.metadata, object=self.object, reversals=self.reversals, reversed=self.reversed, source_transaction=self.source_transaction, source_type=self.source_type, transfer_group=self.transfer_group)
__all__ = ['transfer']