from sqlalchemy import Boolean, Column, Integer

class Payment_Flows_Installment_Options(Base):
    __tablename__ = 'payment_flows_installment_options'
    enabled = Column(Boolean)
    plan = Column(PaymentMethodDetailsCardInstallmentsPlan, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Flows_Installment_Options(enabled={enabled!r}, plan={plan!r}, id={id!r})'.format(enabled=self.enabled, plan=self.plan, id=self.id)
__all__ = ['payment_flows_installment_options']