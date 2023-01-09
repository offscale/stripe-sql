from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_pages_checkout_session_custom_text_position import (
    PaymentPagesCheckoutSessionCustomTextPosition,
)

from . import Base


class PaymentPagesCheckoutSessionCustomText(Base):
    __tablename__ = "payment_pages_checkout_session_custom_text"
    shipping_address = Column(
        PaymentPagesCheckoutSessionCustomTextPosition,
        comment="[[FK(PaymentPagesCheckoutSessionCustomTextPosition)]] Custom text that should be displayed alongside shipping address collection",
        nullable=True,
    )
    submit = Column(
        PaymentPagesCheckoutSessionCustomTextPosition,
        comment="[[FK(PaymentPagesCheckoutSessionCustomTextPosition)]] Custom text that should be displayed alongside the payment confirmation button",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionCustomText(shipping_address={shipping_address!r}, submit={submit!r}, id={id!r})".format(
            shipping_address=self.shipping_address, submit=self.submit, id=self.id
        )


__all__ = ["payment_pages_checkout_session_custom_text"]
