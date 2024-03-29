from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoiceSettingCustomFieldJson = Table(
    "invoice_setting_custom_fieldjson",
    metadata,
    Column("name", String, comment="The name of the custom field"),
    Column("value", String, comment="The value of the custom field"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_setting_custom_field.json"]
