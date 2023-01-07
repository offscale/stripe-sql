from sqlalchemy import Column, Integer, String


class Invoices_From_Invoice(Base):
    __tablename__ = "invoices_from_invoice"
    action = Column(
        String, comment="The relation between this invoice and the cloned invoice"
    )
    invoice = Column(invoice, comment="[[FK(invoice)]] The invoice that was cloned")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoices_From_Invoice(action={action!r}, invoice={invoice!r}, id={id!r})".format(
            action=self.action, invoice=self.invoice, id=self.id
        )


__all__ = ["invoices_from_invoice"]
