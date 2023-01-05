from sqlalchemy import Column, Integer


class Invoice_Threshold_Reason(Base):
    __tablename__ = "invoice_threshold_reason"
    amount_gte = Column(
        Integer,
        comment="The total invoice amount threshold boundary if it triggered the threshold invoice",
        nullable=True,
    )
    item_reasons = Column(
        list, comment="Indicates which line items triggered a threshold invoice"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Threshold_Reason(amount_gte={amount_gte!r}, item_reasons={item_reasons!r}, id={id!r})".format(
            amount_gte=self.amount_gte, item_reasons=self.item_reasons, id=self.id
        )


__all__ = ["invoice_threshold_reason"]
