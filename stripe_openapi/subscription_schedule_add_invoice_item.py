from sqlalchemy import Column, ForeignKey, Identity, Integer, Table, list

from stripe_openapi.price import Price

from . import metadata

SubscriptionScheduleAddInvoiceItem.Json = Table(
    "subscription_schedule_add_invoice_item.json",
    metadata,
    Column(
        "price",
        Price,
        ForeignKey("DeletedPrice"),
        comment="ID of the price used to generate the invoice item",
    ),
    Column(
        "quantity", Integer, comment="The quantity of the invoice item", nullable=True
    ),
    Column(
        "tax_rates",
        list,
        comment="The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedule_add_invoice_item.json"]
