from sqlalchemy import Column, Integer


class Payment_Pages_Checkout_Session_Total_Details(Base):
    __tablename__ = "payment_pages_checkout_session_total_details"
    amount_discount = Column(Integer, comment="This is the sum of all the discounts")
    amount_shipping = Column(
        Integer, comment="This is the sum of all the shipping amounts", nullable=True
    )
    amount_tax = Column(Integer, comment="This is the sum of all the tax amounts")
    breakdown = Column(
        PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown, nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Pages_Checkout_Session_Total_Details(amount_discount={amount_discount!r}, amount_shipping={amount_shipping!r}, amount_tax={amount_tax!r}, breakdown={breakdown!r}, id={id!r})".format(
            amount_discount=self.amount_discount,
            amount_shipping=self.amount_shipping,
            amount_tax=self.amount_tax,
            breakdown=self.breakdown,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_total_details"]
