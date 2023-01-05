from sqlalchemy import Column, Integer


class Payment_Pages_Checkout_Session_Shipping_Option(Base):
    __tablename__ = "payment_pages_checkout_session_shipping_option"
    shipping_amount = Column(
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    )
    shipping_rate = Column(ShippingRate, comment="The shipping rate")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Pages_Checkout_Session_Shipping_Option(shipping_amount={shipping_amount!r}, shipping_rate={shipping_rate!r}, id={id!r})".format(
            shipping_amount=self.shipping_amount,
            shipping_rate=self.shipping_rate,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_shipping_option"]
