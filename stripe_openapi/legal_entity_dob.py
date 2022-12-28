from sqlalchemy import Column, Integer

class Legal_Entity_Dob(Base):
    __tablename__ = 'legal_entity_dob'
    day = Column(Integer, comment='The day of birth, between 1 and 31', nullable=True)
    month = Column(Integer, comment='The month of birth, between 1 and 12', nullable=True)
    year = Column(Integer, comment='The four-digit year of birth', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Legal_Entity_Dob(day={day!r}, month={month!r}, year={year!r}, id={id!r})'.format(day=self.day, month=self.month, year=self.year, id=self.id)
__all__ = ['legal_entity_dob']