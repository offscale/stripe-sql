from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentPagesCheckoutSessionTotalDetails(Base):
    __tablename__ = "payment_pages_checkout_session_total_details"
    amount_discount = Column(Integer, comment="This is the sum of all the discounts")
    amount_shipping = Column(
        Integer, comment="This is the sum of all the shipping amounts", nullable=True
    )
    amount_tax = Column(Integer, comment="This is the sum of all the tax amounts")
    breakdown = Column(
        Integer,
        ForeignKey(
            "payment_pages_checkout_session_total_details_resource_breakdown.id"
        ),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionTotalDetails(amount_discount={amount_discount!r}, amount_shipping={amount_shipping!r}, amount_tax={amount_tax!r}, breakdown={breakdown!r}, id={id!r})".format(
            amount_discount=self.amount_discount,
            amount_shipping=self.amount_shipping,
            amount_tax=self.amount_tax,
            breakdown=self.breakdown,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_total_details"]
