from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

LegalEntityUboDeclaration.Json = Table(
    "legal_entity_ubo_declaration.json",
    metadata,
    Column(
        "date",
        Integer,
        comment="The Unix timestamp marking when the beneficial owner attestation was made",
        nullable=True,
    ),
    Column(
        "ip",
        String,
        comment="The IP address from which the beneficial owner attestation was made",
        nullable=True,
    ),
    Column(
        "user_agent",
        String,
        comment="The user-agent string from the browser where the beneficial owner attestation was made",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_ubo_declaration.json"]
