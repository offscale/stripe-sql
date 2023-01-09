from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class TreasurySharedResourceBillingDetails(Base):
    __tablename__ = "treasury_shared_resource_billing_details"
    address = Column(Address, ForeignKey("Address"))
    email = Column(String, comment="Email address", nullable=True)
    name = Column(String, comment="Full name", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasurySharedResourceBillingDetails(address={address!r}, email={email!r}, name={name!r}, id={id!r})".format(
            address=self.address, email=self.email, name=self.name, id=self.id
        )


__all__ = ["treasury_shared_resource_billing_details"]
