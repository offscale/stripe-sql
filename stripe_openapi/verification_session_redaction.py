from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

VerificationSessionRedactionJson = Table(
    "verification_session_redactionjson",
    metadata,
    Column(
        "status",
        String,
        comment="Indicates whether this object and its related objects have been redacted or not",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["verification_session_redaction.json"]
