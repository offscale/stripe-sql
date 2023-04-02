from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodIdealJson = Table(
    "payment_method_idealjson",
    metadata,
    Column(
        "bank",
        String,
        comment="The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`",
        nullable=True,
    ),
    Column(
        "bic",
        String,
        comment="The Bank Identifier Code of the customer's bank, if the bank was provided",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_ideal.json"]
