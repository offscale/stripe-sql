from sqlalchemy import Column, Integer, String

class Payment_Method_Options_Card_Mandate_Options(Base):
    __tablename__ = 'payment_method_options_card_mandate_options'
    amount = Column(Integer, comment='Amount to be charged for future payments')
    amount_type = Column(String, comment='One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param')
    description = Column(String, comment='A description of the mandate or subscription that is meant to be displayed to the customer', nullable=True)
    end_date = Column(Integer, comment='End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date', nullable=True)
    interval = Column(String, comment='Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`')
    interval_count = Column(Integer, comment='The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`', nullable=True)
    reference = Column(String, comment='Unique identifier for the mandate or subscription')
    start_date = Column(Integer, comment='Start date of the mandate or subscription. Start date should not be lesser than yesterday')
    supported_types = Column(ARRAY(String), comment='Specifies the type of mandates supported. Possible values are `india`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Options_Card_Mandate_Options(amount={amount!r}, amount_type={amount_type!r}, description={description!r}, end_date={end_date!r}, interval={interval!r}, interval_count={interval_count!r}, reference={reference!r}, start_date={start_date!r}, supported_types={supported_types!r}, id={id!r})'.format(amount=self.amount, amount_type=self.amount_type, description=self.description, end_date=self.end_date, interval=self.interval, interval_count=self.interval_count, reference=self.reference, start_date=self.start_date, supported_types=self.supported_types, id=self.id)
__all__ = ['payment_method_options_card_mandate_options']