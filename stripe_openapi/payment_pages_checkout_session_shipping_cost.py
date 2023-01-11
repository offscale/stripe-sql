from sqlalchemy import Column, ForeignKey, Identity, Integer, list

from . import Base


class PaymentPagesCheckoutSessionShippingCost(Base):
    __tablename__ = "payment_pages_checkout_session_shipping_cost"
    amount_subtotal = Column(
        Integer, comment="Total shipping cost before any discounts or taxes are applied"
    )
    amount_tax = Column(
        Integer,
        comment="Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0",
    )
    amount_total = Column(
        Integer, comment="Total shipping cost after discounts and taxes are applied"
    )
    shipping_rate = Column(
        String,
        ForeignKey("shipping_rate.id"),
        comment="The ID of the ShippingRate for this order",
        nullable=True,
    )
    taxes = Column(
        list, comment="The taxes applied to the shipping rate", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionShippingCost(amount_subtotal={amount_subtotal!r}, amount_tax={amount_tax!r}, amount_total={amount_total!r}, shipping_rate={shipping_rate!r}, taxes={taxes!r}, id={id!r})".format(
            amount_subtotal=self.amount_subtotal,
            amount_tax=self.amount_tax,
            amount_total=self.amount_total,
            shipping_rate=self.shipping_rate,
            taxes=self.taxes,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_shipping_cost"]
