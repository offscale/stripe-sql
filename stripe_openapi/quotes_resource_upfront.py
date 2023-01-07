from sqlalchemy import Column, Integer


class Quotes_Resource_Upfront(Base):
    __tablename__ = "quotes_resource_upfront"
    amount_subtotal = Column(
        Integer, comment="Total before any discounts or taxes are applied"
    )
    amount_total = Column(
        Integer, comment="Total after discounts and taxes are applied"
    )
    line_items = Column(
        JSON,
        comment="The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice",
        nullable=True,
    )
    total_details = Column(
        quotes_resource_total_details, ForeignKey("quotes_resource_total_details")
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Quotes_Resource_Upfront(amount_subtotal={amount_subtotal!r}, amount_total={amount_total!r}, line_items={line_items!r}, total_details={total_details!r}, id={id!r})".format(
            amount_subtotal=self.amount_subtotal,
            amount_total=self.amount_total,
            line_items=self.line_items,
            total_details=self.total_details,
            id=self.id,
        )


__all__ = ["quotes_resource_upfront"]
