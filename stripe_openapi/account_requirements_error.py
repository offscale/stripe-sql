from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AccountRequirementsError.Json = Table(
    "account_requirements_error.json",
    metadata,
    Column("code", String, comment="The code for the type of error"),
    Column(
        "reason",
        String,
        comment="An informative message that indicates the error type and provides additional details about the error",
    ),
    Column(
        "requirement",
        String,
        comment="The specific user onboarding requirement field (in the requirements hash) that needs to be resolved",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_requirements_error.json"]
