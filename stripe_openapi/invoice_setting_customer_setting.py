from sqlalchemy import Column, ForeignKey, Identity, Integer, String, list

from . import Base


class InvoiceSettingCustomerSetting(Base):
    __tablename__ = "invoice_setting_customer_setting"
    custom_fields = Column(
        list,
        comment="Default custom fields to be displayed on invoices for this customer",
        nullable=True,
    )
    default_payment_method = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices",
        nullable=True,
    )
    footer = Column(
        String,
        comment="Default footer to be displayed on invoices for this customer",
        nullable=True,
    )
    rendering_options = Column(
        Integer,
        ForeignKey("invoice_setting_rendering_options.id"),
        comment="Default options for invoice PDF rendering for this customer",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoiceSettingCustomerSetting(custom_fields={custom_fields!r}, default_payment_method={default_payment_method!r}, footer={footer!r}, rendering_options={rendering_options!r}, id={id!r})".format(
            custom_fields=self.custom_fields,
            default_payment_method=self.default_payment_method,
            footer=self.footer,
            rendering_options=self.rendering_options,
            id=self.id,
        )


__all__ = ["invoice_setting_customer_setting"]
