from sqlalchemy import Column, String


class Source_Owner(Base):
    __tablename__ = "source_owner"
    address = Column(Address, comment="Owner's address", nullable=True)
    email = Column(String, comment="Owner's email address", nullable=True)
    name = Column(String, comment="Owner's full name", nullable=True)
    phone = Column(
        String, comment="Owner's phone number (including extension)", nullable=True
    )
    verified_address = Column(
        Address,
        comment="Verified owner's address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    verified_email = Column(
        String,
        comment="Verified owner's email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    verified_name = Column(
        String,
        comment="Verified owner's full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
        primary_key=True,
    )
    verified_phone = Column(
        String,
        comment="Verified owner's phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Owner(address={address!r}, email={email!r}, name={name!r}, phone={phone!r}, verified_address={verified_address!r}, verified_email={verified_email!r}, verified_name={verified_name!r}, verified_phone={verified_phone!r})".format(
            address=self.address,
            email=self.email,
            name=self.name,
            phone=self.phone,
            verified_address=self.verified_address,
            verified_email=self.verified_email,
            verified_name=self.verified_name,
            verified_phone=self.verified_phone,
        )


__all__ = ["source_owner"]
