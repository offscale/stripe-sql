from sqlalchemy import Column, Integer, String

class Quotes_Resource_Subscription_Data_Subscription_Data(Base):
    __tablename__ = 'quotes_resource_subscription_data_subscription_data'
    description = Column(String, comment="The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription", nullable=True)
    effective_date = Column(Integer, comment='When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. This date is ignored if it is in the past when the quote is accepted. Measured in seconds since the Unix epoch', nullable=True)
    trial_period_days = Column(Integer, comment='Integer representing the number of trial period days before the customer is charged for the first time', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Quotes_Resource_Subscription_Data_Subscription_Data(description={description!r}, effective_date={effective_date!r}, trial_period_days={trial_period_days!r}, id={id!r})'.format(description=self.description, effective_date=self.effective_date, trial_period_days=self.trial_period_days, id=self.id)
__all__ = ['quotes_resource_subscription_data_subscription_data']