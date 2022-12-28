from sqlalchemy import Column, Integer, String

class Mandate_Acss_Debit(Base):
    __tablename__ = 'mandate_acss_debit'
    default_for = Column(ARRAY(String), comment='List of Stripe products where this mandate can be selected automatically', nullable=True)
    interval_description = Column(String, comment="Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'", nullable=True)
    payment_schedule = Column(String, comment='Payment schedule for the mandate')
    transaction_type = Column(String, comment='Transaction type of the mandate')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Mandate_Acss_Debit(default_for={default_for!r}, interval_description={interval_description!r}, payment_schedule={payment_schedule!r}, transaction_type={transaction_type!r}, id={id!r})'.format(default_for=self.default_for, interval_description=self.interval_description, payment_schedule=self.payment_schedule, transaction_type=self.transaction_type, id=self.id)
__all__ = ['mandate_acss_debit']