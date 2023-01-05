from sqlalchemy import Boolean, Column, Integer, String


class Deleted_Discount(Base):
    __tablename__ = "deleted_discount"
    checkout_session = Column(
        String,
        comment="The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode",
        nullable=True,
    )
    coupon = Column(Coupon)
    customer = Column(
        string | Customer,
        comment="The ID of the customer associated with this discount",
        nullable=True,
    )
    deleted = Column(Boolean, comment="Always true for a deleted object")
    id = Column(
        String,
        comment="The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array",
        primary_key=True,
    )
    invoice = Column(
        String,
        comment="The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice",
        nullable=True,
    )
    invoice_item = Column(
        String,
        comment="The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    promotion_code = Column(
        PromotionCode,
        comment="The promotion code applied to create this discount",
        nullable=True,
    )
    start = Column(Integer, comment="Date that the coupon was applied")
    subscription = Column(
        String,
        comment="The subscription that this coupon is applied to, if it is applied to a particular subscription",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Deleted_Discount(checkout_session={checkout_session!r}, coupon={coupon!r}, customer={customer!r}, deleted={deleted!r}, id={id!r}, invoice={invoice!r}, invoice_item={invoice_item!r}, object={object!r}, promotion_code={promotion_code!r}, start={start!r}, subscription={subscription!r})".format(
            checkout_session=self.checkout_session,
            coupon=self.coupon,
            customer=self.customer,
            deleted=self.deleted,
            id=self.id,
            invoice=self.invoice,
            invoice_item=self.invoice_item,
            object=self.object,
            promotion_code=self.promotion_code,
            start=self.start,
            subscription=self.subscription,
        )


__all__ = ["deleted_discount"]
