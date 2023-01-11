from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class InvoicesLineItemsProrationDetails(Base):
    __tablename__ = "invoices_line_items_proration_details"
    credited_items = Column(
        Integer,
        ForeignKey("invoices_line_items_credited_items.id"),
        comment="For a credit proration `line_item`, the original debit line_items to which the credit proration applies",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicesLineItemsProrationDetails(credited_items={credited_items!r}, id={id!r})".format(
            credited_items=self.credited_items, id=self.id
        )


__all__ = ["invoices_line_items_proration_details"]
