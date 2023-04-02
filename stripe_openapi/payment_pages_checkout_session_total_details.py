from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionTotalDetailsJson = Table(
    "payment_pages_checkout_session_total_detailsjson",
    metadata,
    Column("amount_discount", Integer, comment="This is the sum of all the discounts"),
    Column(
        "amount_shipping",
        Integer,
        comment="This is the sum of all the shipping amounts",
        nullable=True,
    ),
    Column("amount_tax", Integer, comment="This is the sum of all the tax amounts"),
    Column(
        "breakdown",
        PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown,
        ForeignKey("PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_total_details.json"]
