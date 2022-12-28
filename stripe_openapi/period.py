from sqlalchemy import Column, Integer

class Period(Base):
    __tablename__ = 'period'
    end = Column(Integer, comment='The end date of this usage period. All usage up to and including this point in time is included', nullable=True)
    start = Column(Integer, comment='The start date of this usage period. All usage after this point in time is included', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Period(end={end!r}, start={start!r}, id={id!r})'.format(end=self.end, start=self.start, id=self.id)
__all__ = ['period']