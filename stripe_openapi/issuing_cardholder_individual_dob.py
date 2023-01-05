from sqlalchemy import Column, Integer


class Issuing_Cardholder_Individual_Dob(Base):
    __tablename__ = "issuing_cardholder_individual_dob"
    day = Column(Integer, comment="The day of birth, between 1 and 31", nullable=True)
    month = Column(
        Integer, comment="The month of birth, between 1 and 12", nullable=True
    )
    year = Column(Integer, comment="The four-digit year of birth", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Cardholder_Individual_Dob(day={day!r}, month={month!r}, year={year!r}, id={id!r})".format(
            day=self.day, month=self.month, year=self.year, id=self.id
        )


__all__ = ["issuing_cardholder_individual_dob"]
