from sqlalchemy import Column, Integer, String

class Payment_Intent_Payment_Method_Options_Mandate_Options_Acss_Debit(Base):
    __tablename__ = 'payment_intent_payment_method_options_mandate_options_acss_debit'
    custom_mandate_url = Column(String, comment='A URL for custom mandate text', nullable=True)
    interval_description = Column(String, comment="Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'", nullable=True)
    payment_schedule = Column(String, comment='Payment schedule for the mandate', nullable=True)
    transaction_type = Column(String, comment='Transaction type of the mandate', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Intent_Payment_Method_Options_Mandate_Options_Acss_Debit(custom_mandate_url={custom_mandate_url!r}, interval_description={interval_description!r}, payment_schedule={payment_schedule!r}, transaction_type={transaction_type!r}, id={id!r})'.format(custom_mandate_url=self.custom_mandate_url, interval_description=self.interval_description, payment_schedule=self.payment_schedule, transaction_type=self.transaction_type, id=self.id)
__all__ = ['payment_intent_payment_method_options_mandate_options_acss_debit']