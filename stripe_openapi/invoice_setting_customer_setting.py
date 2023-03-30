from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table, list

from . import metadata

InvoiceSettingCustomerSetting.Json = Table(
    "invoice_setting_customer_setting.json",
    metadata,
    Column(
        "custom_fields",
        list,
        comment="Default custom fields to be displayed on invoices for this customer",
        nullable=True,
    ),
    Column(
        "default_payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices",
        nullable=True,
    ),
    Column(
        "footer",
        String,
        comment="Default footer to be displayed on invoices for this customer",
        nullable=True,
    ),
    Column(
        "rendering_options",
        InvoiceSettingRenderingOptions,
        ForeignKey("InvoiceSettingRenderingOptions"),
        comment="Default options for invoice PDF rendering for this customer",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_setting_customer_setting.json"]
