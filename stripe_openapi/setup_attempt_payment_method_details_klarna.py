from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsKlarnaJson = Table(
    "setup_attempt_payment_method_details_klarnajson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_klarna.json"]
