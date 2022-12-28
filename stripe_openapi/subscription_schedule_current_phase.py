from sqlalchemy import Column, Integer

class Subscription_Schedule_Current_Phase(Base):
    __tablename__ = 'subscription_schedule_current_phase'
    end_date = Column(Integer, comment='The end of this phase of the subscription schedule')
    start_date = Column(Integer, comment='The start of this phase of the subscription schedule')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Subscription_Schedule_Current_Phase(end_date={end_date!r}, start_date={start_date!r}, id={id!r})'.format(end_date=self.end_date, start_date=self.start_date, id=self.id)
__all__ = ['subscription_schedule_current_phase']