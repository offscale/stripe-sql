from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodCardChecksJson = Table(
    "payment_method_card_checksjson",
    metadata,
    Column(
        "address_line1_check",
        String,
        comment="If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    ),
    Column(
        "address_postal_code_check",
        String,
        comment="If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    ),
    Column(
        "cvc_check",
        String,
        comment="If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_checks.json"]
