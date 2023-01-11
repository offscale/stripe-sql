from sqlalchemy import Column, ForeignKey, Integer, String

from . import Base


class Discount(Base):
    """
    A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).

    It contains information about when the discount began, when it will end, and what it is applied to.

    Related guide: [Applying Discounts to Subscriptions](https://stripe.com/docs/billing/subscriptions/discounts).

    """

    __tablename__ = "discount"
    checkout_session = Column(
        String,
        comment="The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode",
        nullable=True,
    )
    coupon = Column(Coupon, ForeignKey("Coupon"))
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The ID of the customer associated with this discount",
        nullable=True,
    )
    end = Column(
        Integer,
        comment="If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null",
        nullable=True,
    )
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
        String,
        ForeignKey("promotion_code.id"),
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
        return "Discount(checkout_session={checkout_session!r}, coupon={coupon!r}, customer={customer!r}, end={end!r}, id={id!r}, invoice={invoice!r}, invoice_item={invoice_item!r}, object={object!r}, promotion_code={promotion_code!r}, start={start!r}, subscription={subscription!r})".format(
            checkout_session=self.checkout_session,
            coupon=self.coupon,
            customer=self.customer,
            end=self.end,
            id=self.id,
            invoice=self.invoice,
            invoice_item=self.invoice_item,
            object=self.object,
            promotion_code=self.promotion_code,
            start=self.start,
            subscription=self.subscription,
        )


__all__ = ["discount"]
