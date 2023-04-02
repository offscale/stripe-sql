from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

AccountRequirementsAlternativeJson = Table(
    "account_requirements_alternativejson",
    metadata,
    Column(
        "alternative_fields_due",
        ARRAY(String),
        comment="Fields that can be provided to satisfy all fields in `original_fields_due`",
    ),
    Column(
        "original_fields_due",
        ARRAY(String),
        comment="Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_requirements_alternative.json"]
