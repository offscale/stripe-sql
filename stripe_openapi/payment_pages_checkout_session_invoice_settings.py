from sqlalchemy import JSON, Column, ForeignKey, String, Table, list

from . import metadata

PaymentPagesCheckoutSessionInvoiceSettings.Json = Table(
    "payment_pages_checkout_session_invoice_settings.json",
    metadata,
    Column(
        "account_tax_ids",
        list,
        comment="The account tax IDs associated with the invoice",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "custom_fields",
        list,
        comment="Custom fields displayed on the invoice",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column("footer", String, comment="Footer displayed on the invoice", nullable=True),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "rendering_options",
        InvoiceSettingRenderingOptions,
        ForeignKey("InvoiceSettingRenderingOptions"),
        comment="Options for invoice PDF rendering",
        nullable=True,
    ),
)
__all__ = ["payment_pages_checkout_session_invoice_settings.json"]
