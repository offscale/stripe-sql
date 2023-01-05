from sqlalchemy import Boolean, Column, Integer


class Invoice_Installments_Card(Base):
    __tablename__ = "invoice_installments_card"
    enabled = Column(
        Boolean,
        comment="Whether Installments are enabled for this Invoice",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Installments_Card(enabled={enabled!r}, id={id!r})".format(
            enabled=self.enabled, id=self.id
        )


__all__ = ["invoice_installments_card"]
