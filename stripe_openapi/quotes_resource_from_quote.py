from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.quote import Quote

from . import metadata

QuotesResourceFromQuote.Json = Table(
    "quotes_resource_from_quote.json",
    metadata,
    Column(
        "is_revision",
        Boolean,
        comment="Whether this quote is a revision of a different quote",
    ),
    Column("quote", Quote, ForeignKey("Quote"), comment="The quote that was cloned"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_from_quote.json"]
