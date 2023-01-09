from sqlalchemy import Boolean, Column, Integer, String, list

from . import Base


class CreditNoteLineItem(Base):
    __tablename__ = "credit_note_line_item"
    amount = Column(
        Integer,
        comment="The integer amount in %s representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts",
    )
    amount_excluding_tax = Column(
        Integer,
        comment="The integer amount in %s representing the amount being credited for this line item, excluding all tax and discounts",
        nullable=True,
    )
    description = Column(
        String, comment="Description of the item being credited", nullable=True
    )
    discount_amount = Column(
        Integer,
        comment="The integer amount in %s representing the discount being credited for this line item",
    )
    discount_amounts = Column(
        list,
        comment="The amount of discount calculated per discount for this line item",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice_line_item = Column(
        String, comment="ID of the invoice line item being credited", nullable=True
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    quantity = Column(
        Integer, comment="The number of units of product being credited", nullable=True
    )
    tax_amounts = Column(
        list, comment="The amount of tax calculated per tax rate for this line item"
    )
    tax_rates = Column(list, comment="The tax rates which apply to the line item")
    type = Column(
        String,
        comment="The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice",
    )
    unit_amount = Column(
        Integer,
        comment="The cost of each unit of product being credited",
        nullable=True,
    )
    unit_amount_decimal = Column(
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    )
    unit_amount_excluding_tax = Column(
        String,
        comment="The amount in %s representing the unit amount being credited for this line item, excluding all tax and discounts",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CreditNoteLineItem(amount={amount!r}, amount_excluding_tax={amount_excluding_tax!r}, description={description!r}, discount_amount={discount_amount!r}, discount_amounts={discount_amounts!r}, id={id!r}, invoice_line_item={invoice_line_item!r}, livemode={livemode!r}, object={object!r}, quantity={quantity!r}, tax_amounts={tax_amounts!r}, tax_rates={tax_rates!r}, type={type!r}, unit_amount={unit_amount!r}, unit_amount_decimal={unit_amount_decimal!r}, unit_amount_excluding_tax={unit_amount_excluding_tax!r})".format(
            amount=self.amount,
            amount_excluding_tax=self.amount_excluding_tax,
            description=self.description,
            discount_amount=self.discount_amount,
            discount_amounts=self.discount_amounts,
            id=self.id,
            invoice_line_item=self.invoice_line_item,
            livemode=self.livemode,
            object=self.object,
            quantity=self.quantity,
            tax_amounts=self.tax_amounts,
            tax_rates=self.tax_rates,
            type=self.type,
            unit_amount=self.unit_amount,
            unit_amount_decimal=self.unit_amount_decimal,
            unit_amount_excluding_tax=self.unit_amount_excluding_tax,
        )


__all__ = ["credit_note_line_item"]
