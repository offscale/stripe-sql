from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingAuthorizationVerificationDataJson = Table(
    "issuing_authorization_verification_datajson",
    metadata,
    Column(
        "address_line1_check",
        String,
        comment="Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`",
    ),
    Column(
        "address_postal_code_check",
        String,
        comment="Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`",
    ),
    Column(
        "cvc_check",
        String,
        comment="Whether the cardholder provided a CVC and if it matched Stripe’s record",
    ),
    Column(
        "expiry_check",
        String,
        comment="Whether the cardholder provided an expiry date and if it matched Stripe’s record",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_authorization_verification_data.json"]
