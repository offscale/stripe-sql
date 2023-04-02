from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.file import File

from . import metadata

IssuingCardholderIdDocumentJson = Table(
    "issuing_cardholder_id_documentjson",
    metadata,
    Column(
        "back",
        File,
        ForeignKey("File"),
        comment="The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    ),
    Column(
        "front",
        File,
        ForeignKey("File"),
        comment="The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_id_document.json"]
