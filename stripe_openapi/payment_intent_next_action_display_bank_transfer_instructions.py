from sqlalchemy import Column, Integer, String

class Payment_Intent_Next_Action_Display_Bank_Transfer_Instructions(Base):
    __tablename__ = 'payment_intent_next_action_display_bank_transfer_instructions'
    amount_remaining = Column(Integer, comment='The remaining amount that needs to be transferred to complete the payment', nullable=True)
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)', nullable=True)
    financial_addresses = Column(list, comment='A list of financial addresses that can be used to fund the customer balance', nullable=True)
    hosted_instructions_url = Column(String, comment='A link to a hosted page that guides your customer through completing the transfer', nullable=True)
    reference = Column(String, comment='A string identifying this payment. Instruct your customer to include this code in the reference or memo field of their bank transfer', nullable=True)
    type = Column(String, comment='Type of bank transfer')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Intent_Next_Action_Display_Bank_Transfer_Instructions(amount_remaining={amount_remaining!r}, currency={currency!r}, financial_addresses={financial_addresses!r}, hosted_instructions_url={hosted_instructions_url!r}, reference={reference!r}, type={type!r}, id={id!r})'.format(amount_remaining=self.amount_remaining, currency=self.currency, financial_addresses=self.financial_addresses, hosted_instructions_url=self.hosted_instructions_url, reference=self.reference, type=self.type, id=self.id)
__all__ = ['payment_intent_next_action_display_bank_transfer_instructions']