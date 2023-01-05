from sqlalchemy import Column, Integer, String


class Source_Receiver_Flow(Base):
    __tablename__ = "source_receiver_flow"
    address = Column(
        String,
        comment="The address of the receiver source. This is the value that should be communicated to the customer to send their funds to",
        nullable=True,
    )
    amount_charged = Column(
        Integer,
        comment="The total amount that was moved to your balance. This is almost always equal to the amount charged. In rare cases when customers deposit excess funds and we are unable to refund those, those funds get moved to your balance and show up in amount_charged as well. The amount charged is expressed in the source's currency",
    )
    amount_received = Column(
        Integer,
        comment="The total amount received by the receiver source. `amount_received = amount_returned + amount_charged` should be true for consumed sources unless customers deposit excess funds. The amount received is expressed in the source's currency",
    )
    amount_returned = Column(
        Integer,
        comment="The total amount that was returned to the customer. The amount returned is expressed in the source's currency",
    )
    refund_attributes_method = Column(
        String,
        comment="Type of refund attribute method, one of `email`, `manual`, or `none`",
    )
    refund_attributes_status = Column(
        String,
        comment="Type of refund attribute status, one of `missing`, `requested`, or `available`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Receiver_Flow(address={address!r}, amount_charged={amount_charged!r}, amount_received={amount_received!r}, amount_returned={amount_returned!r}, refund_attributes_method={refund_attributes_method!r}, refund_attributes_status={refund_attributes_status!r}, id={id!r})".format(
            address=self.address,
            amount_charged=self.amount_charged,
            amount_received=self.amount_received,
            amount_returned=self.amount_returned,
            refund_attributes_method=self.refund_attributes_method,
            refund_attributes_status=self.refund_attributes_status,
            id=self.id,
        )


__all__ = ["source_receiver_flow"]
