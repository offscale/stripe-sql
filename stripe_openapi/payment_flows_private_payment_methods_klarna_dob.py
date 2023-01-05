from sqlalchemy import Column, Integer


class Payment_Flows_Private_Payment_Methods_Klarna_Dob(Base):
    __tablename__ = "payment_flows_private_payment_methods_klarna_dob"
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
        return "Payment_Flows_Private_Payment_Methods_Klarna_Dob(day={day!r}, month={month!r}, year={year!r}, id={id!r})".format(
            day=self.day, month=self.month, year=self.year, id=self.id
        )


__all__ = ["payment_flows_private_payment_methods_klarna_dob"]
