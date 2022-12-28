from sqlalchemy import Boolean, Column, Integer, String

class Issuing_Authorization_Pending_Request(Base):
    __tablename__ = 'issuing_authorization_pending_request'
    amount = Column(Integer, comment="The additional amount Stripe will hold if the authorization is approved, in the card's [currency](https://stripe.com/docs/api#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)")
    amount_details = Column(IssuingAuthorizationAmountDetails, comment='Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)', nullable=True)
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    is_amount_controllable = Column(Boolean, comment='If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization')
    merchant_amount = Column(Integer, comment='The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)')
    merchant_currency = Column(String, comment='The local currency the merchant is requesting to authorize')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Authorization_Pending_Request(amount={amount!r}, amount_details={amount_details!r}, currency={currency!r}, is_amount_controllable={is_amount_controllable!r}, merchant_amount={merchant_amount!r}, merchant_currency={merchant_currency!r}, id={id!r})'.format(amount=self.amount, amount_details=self.amount_details, currency=self.currency, is_amount_controllable=self.is_amount_controllable, merchant_amount=self.merchant_amount, merchant_currency=self.merchant_currency, id=self.id)
__all__ = ['issuing_authorization_pending_request']