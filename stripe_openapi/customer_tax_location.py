from sqlalchemy import Column, Integer, String


class Customer_Tax_Location(Base):
    __tablename__ = "customer_tax_location"
    country = Column(
        String, comment="The customer's country as identified by Stripe Tax"
    )
    source = Column(
        String, comment="The data source used to infer the customer's location"
    )
    state = Column(
        String,
        comment="The customer's state, county, province, or region as identified by Stripe Tax",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Tax_Location(country={country!r}, source={source!r}, state={state!r}, id={id!r})".format(
            country=self.country, source=self.source, state=self.state, id=self.id
        )


__all__ = ["customer_tax_location"]
