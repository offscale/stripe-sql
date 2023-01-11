from sqlalchemy import Column, ForeignKey, Integer, String, list

from . import Base


class Item(Base):
    """
    A line item.
    """

    __tablename__ = "item"
    amount_discount = Column(
        Integer,
        comment="Total discount amount applied. If no discounts were applied, defaults to 0",
    )
    amount_subtotal = Column(
        Integer, comment="Total before any discounts or taxes are applied"
    )
    amount_tax = Column(
        Integer,
        comment="Total tax amount applied. If no tax was applied, defaults to 0",
    )
    amount_total = Column(Integer, comment="Total after discounts and taxes")
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name",
    )
    discounts = Column(
        list, comment="The discounts applied to the line item", nullable=True
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    price = Column(
        Price,
        ForeignKey("Price"),
        comment="The price used to generate the line item",
        nullable=True,
    )
    quantity = Column(
        Integer, comment="The quantity of products being purchased", nullable=True
    )
    taxes = Column(list, comment="The taxes applied to the line item", nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Item(amount_discount={amount_discount!r}, amount_subtotal={amount_subtotal!r}, amount_tax={amount_tax!r}, amount_total={amount_total!r}, currency={currency!r}, description={description!r}, discounts={discounts!r}, id={id!r}, object={object!r}, price={price!r}, quantity={quantity!r}, taxes={taxes!r})".format(
            amount_discount=self.amount_discount,
            amount_subtotal=self.amount_subtotal,
            amount_tax=self.amount_tax,
            amount_total=self.amount_total,
            currency=self.currency,
            description=self.description,
            discounts=self.discounts,
            id=self.id,
            object=self.object,
            price=self.price,
            quantity=self.quantity,
            taxes=self.taxes,
        )


__all__ = ["item"]
