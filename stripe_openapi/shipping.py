from sqlalchemy import Column, Integer, String


class Shipping(Base):
    __tablename__ = "shipping"
    address = Column(address, ForeignKey("address"), nullable=True)
    carrier = Column(
        String,
        comment="The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc",
        nullable=True,
    )
    name = Column(String, comment="Recipient name", nullable=True)
    phone = Column(
        String, comment="Recipient phone (including extension)", nullable=True
    )
    tracking_number = Column(
        String,
        comment="The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Shipping(address={address!r}, carrier={carrier!r}, name={name!r}, phone={phone!r}, tracking_number={tracking_number!r}, id={id!r})".format(
            address=self.address,
            carrier=self.carrier,
            name=self.name,
            phone=self.phone,
            tracking_number=self.tracking_number,
            id=self.id,
        )


__all__ = ["shipping"]
