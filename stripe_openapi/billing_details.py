from sqlalchemy import Column, Identity, Integer, String

from . import Base


class BillingDetails(Base):
    __tablename__ = "billing_details"
    address = Column(Address, comment="[[FK(Address)]] Billing address", nullable=True)
    email = Column(String, comment="Email address", nullable=True)
    name = Column(String, comment="Full name", nullable=True)
    phone = Column(
        String, comment="Billing phone number (including extension)", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "BillingDetails(address={address!r}, email={email!r}, name={name!r}, phone={phone!r}, id={id!r})".format(
            address=self.address,
            email=self.email,
            name=self.name,
            phone=self.phone,
            id=self.id,
        )


__all__ = ["billing_details"]
