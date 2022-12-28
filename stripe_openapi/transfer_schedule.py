from sqlalchemy import Column, Integer, String

class Transfer_Schedule(Base):
    __tablename__ = 'transfer_schedule'
    delay_days = Column(Integer, comment='The number of days charges for the account will be held before being paid out')
    interval = Column(String, comment='How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`')
    monthly_anchor = Column(Integer, comment='The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months', nullable=True)
    weekly_anchor = Column(String, comment="The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Transfer_Schedule(delay_days={delay_days!r}, interval={interval!r}, monthly_anchor={monthly_anchor!r}, weekly_anchor={weekly_anchor!r}, id={id!r})'.format(delay_days=self.delay_days, interval=self.interval, monthly_anchor=self.monthly_anchor, weekly_anchor=self.weekly_anchor, id=self.id)
__all__ = ['transfer_schedule']