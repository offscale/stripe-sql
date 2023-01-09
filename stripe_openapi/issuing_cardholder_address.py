from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class IssuingCardholderAddress(Base):
    __tablename__ = "issuing_cardholder_address"
    address = Column(Address, ForeignKey("Address"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderAddress(address={address!r}, id={id!r})".format(
            address=self.address, id=self.id
        )


__all__ = ["issuing_cardholder_address"]
