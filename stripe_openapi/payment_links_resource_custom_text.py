from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_links_resource_custom_text_position import (
    PaymentLinksResourceCustomTextPosition,
)

from . import Base


class PaymentLinksResourceCustomText(Base):
    __tablename__ = "payment_links_resource_custom_text"
    shipping_address = Column(
        PaymentLinksResourceCustomTextPosition,
        comment="[[FK(PaymentLinksResourceCustomTextPosition)]] Custom text that should be displayed alongside shipping address collection",
        nullable=True,
    )
    submit = Column(
        PaymentLinksResourceCustomTextPosition,
        comment="[[FK(PaymentLinksResourceCustomTextPosition)]] Custom text that should be displayed alongside the payment confirmation button",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceCustomText(shipping_address={shipping_address!r}, submit={submit!r}, id={id!r})".format(
            shipping_address=self.shipping_address, submit=self.submit, id=self.id
        )


__all__ = ["payment_links_resource_custom_text"]
