from sqlalchemy import Column, Integer


class Invoice_Item_Threshold_Reason(Base):
    __tablename__ = "invoice_item_threshold_reason"
    line_item_ids = Column(
        ARRAY(String),
        comment="The IDs of the line items that triggered the threshold invoice",
        primary_key=True,
    )
    usage_gte = Column(
        Integer,
        comment="The quantity threshold boundary that applied to the given line item",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Item_Threshold_Reason(line_item_ids={line_item_ids!r}, usage_gte={usage_gte!r})".format(
            line_item_ids=self.line_item_ids, usage_gte=self.usage_gte
        )


__all__ = ["invoice_item_threshold_reason"]
