from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SubscriptionPendingInvoiceItemIntervalJson = Table(
    "subscription_pending_invoice_item_intervaljson",
    metadata,
    Column(
        "interval",
        String,
        comment="Specifies invoicing frequency. Either `day`, `week`, `month` or `year`",
    ),
    Column(
        "interval_count",
        Integer,
        comment="The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks)",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_pending_invoice_item_interval.json"]
