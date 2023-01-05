from sqlalchemy import Boolean, Column, Integer, String


class Issuing_Card_Shipping(Base):
    __tablename__ = "issuing_card_shipping"
    address = Column(Address)
    carrier = Column(
        String, comment="The delivery company that shipped a card", nullable=True
    )
    customs = Column(
        IssuingCardShippingCustoms,
        comment="Additional information that may be required for clearing customs",
        nullable=True,
    )
    eta = Column(
        Integer,
        comment="A unix timestamp representing a best estimate of when the card will be delivered",
        nullable=True,
    )
    name = Column(String, comment="Recipient name")
    phone_number = Column(
        String,
        comment="The phone number of the receiver of the bulk shipment. This phone number will be provided to the shipping company, who might use it to contact the receiver in case of delivery issues",
        nullable=True,
    )
    require_signature = Column(
        Boolean,
        comment="Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true",
        nullable=True,
    )
    service = Column(
        String, comment="Shipment service, such as `standard` or `express`"
    )
    status = Column(String, comment="The delivery status of the card", nullable=True)
    tracking_number = Column(
        String, comment="A tracking number for a card shipment", nullable=True
    )
    tracking_url = Column(
        String,
        comment="A link to the shipping carrier's site where you can view detailed information about a card shipment",
        nullable=True,
    )
    type = Column(String, comment="Packaging options")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Card_Shipping(address={address!r}, carrier={carrier!r}, customs={customs!r}, eta={eta!r}, name={name!r}, phone_number={phone_number!r}, require_signature={require_signature!r}, service={service!r}, status={status!r}, tracking_number={tracking_number!r}, tracking_url={tracking_url!r}, type={type!r}, id={id!r})".format(
            address=self.address,
            carrier=self.carrier,
            customs=self.customs,
            eta=self.eta,
            name=self.name,
            phone_number=self.phone_number,
            require_signature=self.require_signature,
            service=self.service,
            status=self.status,
            tracking_number=self.tracking_number,
            tracking_url=self.tracking_url,
            type=self.type,
            id=self.id,
        )


__all__ = ["issuing_card_shipping"]
