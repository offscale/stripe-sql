from sqlalchemy import Column, Integer


class Gelato_Data_Id_Number_Report_Date(Base):
    """
    Point in Time
    """

    __tablename__ = "gelato_data_id_number_report_date"
    day = Column(Integer, comment="Numerical day between 1 and 31", nullable=True)
    month = Column(Integer, comment="Numerical month between 1 and 12", nullable=True)
    year = Column(Integer, comment="The four-digit year", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Gelato_Data_Id_Number_Report_Date(day={day!r}, month={month!r}, year={year!r}, id={id!r})".format(
            day=self.day, month=self.month, year=self.year, id=self.id
        )


__all__ = ["gelato_data_id_number_report_date"]
