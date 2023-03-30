from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsGiropay.Json = Table(
    "payment_method_details_giropay.json",
    metadata,
    Column(
        "bank_code",
        String,
        comment="Bank code of bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "bic",
        String,
        comment="Bank Identifier Code of the bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "verified_name",
        String,
        comment="Owner's verified full name. Values are verified or provided by Giropay directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated.\nGiropay rarely provides this information so the attribute is usually empty",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_giropay.json"]
