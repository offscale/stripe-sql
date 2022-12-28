from sqlalchemy import Boolean, Column, Integer

class Payment_Flows_Automatic_Payment_Methods_Payment_Intent(Base):
    __tablename__ = 'payment_flows_automatic_payment_methods_payment_intent'
    enabled = Column(Boolean, comment='Automatically calculates compatible payment methods')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Flows_Automatic_Payment_Methods_Payment_Intent(enabled={enabled!r}, id={id!r})'.format(enabled=self.enabled, id=self.id)
__all__ = ['payment_flows_automatic_payment_methods_payment_intent']