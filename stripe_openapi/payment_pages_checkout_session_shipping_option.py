from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentPagesCheckoutSessionShippingOption(Base):
    __tablename__ = "payment_pages_checkout_session_shipping_option"
    shipping_amount = Column(
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    )
    shipping_rate = Column(
        String, ForeignKey("shipping_rate.id"), comment="The shipping rate"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionShippingOption(shipping_amount={shipping_amount!r}, shipping_rate={shipping_rate!r}, id={id!r})".format(
            shipping_amount=self.shipping_amount,
            shipping_rate=self.shipping_rate,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_shipping_option"]
