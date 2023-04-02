from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoiceSettingRenderingOptionsJson = Table(
    "invoice_setting_rendering_optionsjson",
    metadata,
    Column(
        "amount_tax_display",
        String,
        comment="How line-item prices and amounts will be displayed with respect to tax on invoice PDFs",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_setting_rendering_options.json"]
