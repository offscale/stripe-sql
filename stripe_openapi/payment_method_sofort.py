from sqlalchemy import Column, Integer, String


class Payment_Method_Sofort(Base):
    __tablename__ = "payment_method_sofort"
    country = Column(
        String,
        comment="Two-letter ISO code representing the country the bank account is located in",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Sofort(country={country!r}, id={id!r})".format(
            country=self.country, id=self.id
        )


__all__ = ["payment_method_sofort"]
