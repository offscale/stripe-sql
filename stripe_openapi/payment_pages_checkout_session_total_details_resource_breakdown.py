from sqlalchemy import Column, Identity, Integer, Table, list

from . import metadata

PaymentPagesCheckoutSessionTotalDetailsResourceBreakdownJson = Table(
    "payment_pages_checkout_session_total_details_resource_breakdownjson",
    metadata,
    Column("discounts", list, comment="The aggregated discounts"),
    Column("taxes", list, comment="The aggregated tax amounts by rate"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_total_details_resource_breakdown.json"]
