from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.customer_tax_location import CustomerTaxLocation

from . import Base


class CustomerTax(Base):
    __tablename__ = "customer_tax"
    automatic_tax = Column(
        String,
        comment="Surfaces if automatic tax computation is possible given the current customer location information",
    )
    ip_address = Column(
        String,
        comment="A recent IP address of the customer used for tax reporting and tax location inference",
        nullable=True,
    )
    location = Column(
        CustomerTaxLocation,
        comment="[[FK(CustomerTaxLocation)]] The customer's location as identified by Stripe Tax",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerTax(automatic_tax={automatic_tax!r}, ip_address={ip_address!r}, location={location!r}, id={id!r})".format(
            automatic_tax=self.automatic_tax,
            ip_address=self.ip_address,
            location=self.location,
            id=self.id,
        )


__all__ = ["customer_tax"]
