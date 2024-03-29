from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AlternateStatementDescriptorsJson = Table(
    "alternate_statement_descriptorsjson",
    metadata,
    Column(
        "kana", String, comment="The Kana variation of the descriptor", nullable=True
    ),
    Column(
        "kanji", String, comment="The Kanji variation of the descriptor", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["alternate_statement_descriptors.json"]
