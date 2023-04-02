from sqlalchemy import Column, ForeignKey, Table

from . import metadata

GelatoVerificationSessionOptionsJson = Table(
    "gelato_verification_session_optionsjson",
    metadata,
    Column(
        "document",
        GelatoSessionDocumentOptions,
        ForeignKey("GelatoSessionDocumentOptions"),
        nullable=True,
    ),
    Column(
        "id_number",
        GelatoSessionIdNumberOptions,
        comment="[FK(GelatoSessionIdNumberOptions)]",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["gelato_verification_session_options.json"]
