from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.mandate import Mandate

from . import metadata

PaymentMethodDetailsBancontact.Json = Table(
    "payment_method_details_bancontact.json",
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
        "preferred_language",
        String,
        comment="Preferred language of the Bancontact authorization page that the customer is redirected to.\nCan be one of `en`, `de`, `fr`, or `nl`",
        nullable=True,
    ),
    Column(
        "verified_name",
        String,
        comment="Owner's verified full name. Values are verified or provided by Bancontact directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_bancontact.json"]
