from sqlalchemy import Column, Integer, String


class Invoice_Setting_Customer_Setting(Base):
    __tablename__ = "invoice_setting_customer_setting"
    custom_fields = Column(
        list,
        comment="Default custom fields to be displayed on invoices for this customer",
        nullable=True,
    )
    default_payment_method = Column(
        payment_method,
        comment="[[FK(payment_method)]] ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices",
        nullable=True,
    )
    footer = Column(
        String,
        comment="Default footer to be displayed on invoices for this customer",
        nullable=True,
    )
    rendering_options = Column(
        invoice_setting_rendering_options,
        comment="[[FK(invoice_setting_rendering_options)]] Default options for invoice PDF rendering for this customer",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Setting_Customer_Setting(custom_fields={custom_fields!r}, default_payment_method={default_payment_method!r}, footer={footer!r}, rendering_options={rendering_options!r}, id={id!r})".format(
            custom_fields=self.custom_fields,
            default_payment_method=self.default_payment_method,
            footer=self.footer,
            rendering_options=self.rendering_options,
            id=self.id,
        )


__all__ = ["invoice_setting_customer_setting"]
