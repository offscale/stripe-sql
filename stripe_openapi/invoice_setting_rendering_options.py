from sqlalchemy import Column, Identity, Integer, String

from . import Base


class InvoiceSettingRenderingOptions(Base):
    __tablename__ = "invoice_setting_rendering_options"
    amount_tax_display = Column(
        String,
        comment="How line-item prices and amounts will be displayed with respect to tax on invoice PDFs",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoiceSettingRenderingOptions(amount_tax_display={amount_tax_display!r}, id={id!r})".format(
            amount_tax_display=self.amount_tax_display, id=self.id
        )


__all__ = ["invoice_setting_rendering_options"]
