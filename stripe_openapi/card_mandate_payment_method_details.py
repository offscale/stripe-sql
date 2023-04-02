from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

CardMandatePaymentMethodDetailsJson = Table(
    "card_mandate_payment_method_detailsjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["card_mandate_payment_method_details.json"]
