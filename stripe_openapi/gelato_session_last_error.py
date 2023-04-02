from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

GelatoSessionLastErrorJson = Table(
    "gelato_session_last_errorjson",
    metadata,
    Column(
        "code",
        String,
        comment="A short machine-readable string giving the reason for the verification or user-session failure",
        nullable=True,
    ),
    Column(
        "reason",
        String,
        comment="A message that explains the reason for verification or user-session failure",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_session_last_error.json"]
