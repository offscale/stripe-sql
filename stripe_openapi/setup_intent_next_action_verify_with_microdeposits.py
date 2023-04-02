from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SetupIntentNextActionVerifyWithMicrodepositsJson = Table(
    "setup_intent_next_action_verify_with_microdepositsjson",
    metadata,
    Column(
        "arrival_date",
        Integer,
        comment="The timestamp when the microdeposits are expected to land",
    ),
    Column(
        "hosted_verification_url",
        String,
        comment="The URL for the hosted verification page, which allows customers to verify their bank account",
    ),
    Column(
        "microdeposit_type",
        String,
        comment="The type of the microdeposit sent to the customer. Used to distinguish between different verification methods",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_next_action_verify_with_microdeposits.json"]
