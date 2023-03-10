from sqlalchemy import Column, Identity, Integer

from . import Base


class InvoiceSettingQuoteSetting(Base):
    __tablename__ = "invoice_setting_quote_setting"
    days_until_due = Column(
        Integer,
        comment="Number of days within which a customer must pay invoices generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoiceSettingQuoteSetting(days_until_due={days_until_due!r}, id={id!r})".format(
            days_until_due=self.days_until_due, id=self.id
        )


__all__ = ["invoice_setting_quote_setting"]
