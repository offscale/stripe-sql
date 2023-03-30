from sqlalchemy import Boolean, Column, Float, Identity, Integer, String, Table

from . import metadata

PersonRelationship.Json = Table(
    "person_relationship.json",
    metadata,
    Column(
        "director",
        Boolean,
        comment="Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations",
        nullable=True,
    ),
    Column(
        "executive",
        Boolean,
        comment="Whether the person has significant responsibility to control, manage, or direct the organization",
        nullable=True,
    ),
    Column(
        "owner",
        Boolean,
        comment="Whether the person is an owner of the account’s legal entity",
        nullable=True,
    ),
    Column(
        "percent_ownership",
        Float,
        comment="The percent owned by the person of the account's legal entity",
        nullable=True,
    ),
    Column(
        "representative",
        Boolean,
        comment="Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account",
        nullable=True,
    ),
    Column(
        "title",
        String,
        comment="The person's title (e.g., CEO, Support Engineer)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["person_relationship.json"]
