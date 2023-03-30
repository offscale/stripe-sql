from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

InvoiceSettingQuoteSetting.Json = Table(
    "invoice_setting_quote_setting.json",
    metadata,
    Column(
        "days_until_due",
        Integer,
        comment="Number of days within which a customer must pay invoices generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_setting_quote_setting.json"]
