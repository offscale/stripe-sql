from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

IssuingCardholderRequirements.Json = Table(
    "issuing_cardholder_requirements.json",
    metadata,
    Column(
        "disabled_reason",
        String,
        comment="If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason",
        nullable=True,
    ),
    Column(
        "past_due",
        ARRAY(String),
        comment="Array of fields that need to be collected in order to verify and re-enable the cardholder",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_requirements.json"]
