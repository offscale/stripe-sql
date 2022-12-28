from sqlalchemy import Column, Integer

class Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Refunded_From_Payment_Transaction(Base):
    __tablename__ = 'customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction'
    refund = Column(Refund, comment="The [Refund](https://stripe.com/docs/api/refunds/object) that moved these funds into the customer's cash balance")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Refunded_From_Payment_Transaction(refund={refund!r}, id={id!r})'.format(refund=self.refund, id=self.id)
__all__ = ['customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction']