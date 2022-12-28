from sqlalchemy import Column, Integer, String

class Fee_Refund(Base):
    """
        `Application Fee Refund` objects allow you to refund an application fee that
    
        has previously been created but not yet refunded. Funds will be refunded to
        the Stripe account from which the fee was originally collected.
    
        Related guide: [Refunding Application Fees](https://stripe.com/docs/connect/destination-charges#refunding-app-fee).
    
        """
    __tablename__ = 'fee_refund'
    amount = Column(Integer, comment='Amount, in %s')
    balance_transaction = Column(BalanceTransaction, comment='Balance transaction that describes the impact on your account balance', nullable=True)
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    fee = Column(ApplicationFee, comment='ID of the application fee that was refunded')
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format', nullable=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Fee_Refund(amount={amount!r}, balance_transaction={balance_transaction!r}, created={created!r}, currency={currency!r}, fee={fee!r}, id={id!r}, metadata={metadata!r}, object={object!r})'.format(amount=self.amount, balance_transaction=self.balance_transaction, created=self.created, currency=self.currency, fee=self.fee, id=self.id, metadata=self.metadata, object=self.object)
__all__ = ['fee_refund']