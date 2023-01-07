from sqlalchemy import Column, String


class Payment_Pages_Checkout_Session_Invoice_Settings(Base):
    __tablename__ = "payment_pages_checkout_session_invoice_settings"
    account_tax_ids = Column(
        list,
        comment="The account tax IDs associated with the invoice",
        nullable=True,
        primary_key=True,
    )
    custom_fields = Column(
        list, comment="Custom fields displayed on the invoice", nullable=True
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    footer = Column(String, comment="Footer displayed on the invoice", nullable=True)
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    rendering_options = Column(
        invoice_setting_rendering_options,
        comment="[[FK(invoice_setting_rendering_options)]] Options for invoice PDF rendering",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Pages_Checkout_Session_Invoice_Settings(account_tax_ids={account_tax_ids!r}, custom_fields={custom_fields!r}, description={description!r}, footer={footer!r}, metadata={metadata!r}, rendering_options={rendering_options!r})".format(
            account_tax_ids=self.account_tax_ids,
            custom_fields=self.custom_fields,
            description=self.description,
            footer=self.footer,
            metadata=self.metadata,
            rendering_options=self.rendering_options,
        )


__all__ = ["payment_pages_checkout_session_invoice_settings"]
