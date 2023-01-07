from sqlalchemy import Column, Integer


class Quotes_Resource_Computed(Base):
    __tablename__ = "quotes_resource_computed"
    recurring = Column(
        quotes_resource_recurring,
        comment="[[FK(quotes_resource_recurring)]] The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices",
        nullable=True,
    )
    upfront = Column(quotes_resource_upfront, ForeignKey("quotes_resource_upfront"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Quotes_Resource_Computed(recurring={recurring!r}, upfront={upfront!r}, id={id!r})".format(
            recurring=self.recurring, upfront=self.upfront, id=self.id
        )


__all__ = ["quotes_resource_computed"]
