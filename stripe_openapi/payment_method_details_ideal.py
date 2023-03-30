from sqlalchemy import Column, ForeignKey, String, Table

from stripe_openapi.mandate import Mandate

from . import metadata

PaymentMethodDetailsIdeal.Json = Table(
    "payment_method_details_ideal.json",
    metadata,
    Column(
        "bank",
        String,
        comment="The customer's bank. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`",
        nullable=True,
    ),
    Column(
        "bic",
        String,
        comment="The Bank Identifier Code of the customer's bank",
        nullable=True,
    ),
    Column(
        "generated_sepa_debit",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge",
        nullable=True,
    ),
    Column(
        "generated_sepa_debit_mandate",
        Mandate,
        ForeignKey("Mandate"),
        comment="The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge",
        nullable=True,
    ),
    Column(
        "iban_last4", String, comment="Last four characters of the IBAN", nullable=True
    ),
    Column(
        "verified_name",
        String,
        comment="Owner's verified full name. Values are verified or provided by iDEAL directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["payment_method_details_ideal.json"]
