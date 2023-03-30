from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

EmailSent.Json = Table(
    "email_sent.json",
    metadata,
    Column("email_sent_at", Integer, comment="The timestamp when the email was sent"),
    Column("email_sent_to", String, comment="The recipient's email address"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["email_sent.json"]
