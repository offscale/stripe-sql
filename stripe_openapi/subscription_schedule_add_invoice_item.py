from sqlalchemy import Column, Integer


class Subscription_Schedule_Add_Invoice_Item(Base):
    """
    An Add Invoice Item describes the prices and quantities that will be added as pending invoice items when entering a phase.
    """

    __tablename__ = "subscription_schedule_add_invoice_item"
    price = Column(
        string | price,
        comment="[[FK(deleted_price)]] ID of the price used to generate the invoice item",
    )
    quantity = Column(
        Integer, comment="The quantity of the invoice item", nullable=True
    )
    tax_rates = Column(
        list,
        comment="The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Schedule_Add_Invoice_Item(price={price!r}, quantity={quantity!r}, tax_rates={tax_rates!r}, id={id!r})".format(
            price=self.price,
            quantity=self.quantity,
            tax_rates=self.tax_rates,
            id=self.id,
        )


__all__ = ["subscription_schedule_add_invoice_item"]
