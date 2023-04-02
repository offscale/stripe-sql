from sqlalchemy import JSON, Column, Integer, String, Table

from . import metadata

FileJson = Table(
    "filejson",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "expires_at",
        Integer,
        comment="The time at which the file expires and is no longer available in epoch seconds",
        nullable=True,
    ),
    Column(
        "filename",
        String,
        comment="A filename for the file, suitable for saving to a filesystem",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "links",
        JSON,
        comment="A list of [file links](https://stripe.com/docs/api#file_links) that point at this file",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "purpose",
        String,
        comment="The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file",
    ),
    Column("size", Integer, comment="The size in bytes of the file object"),
    Column(
        "title", String, comment="A user friendly title for the document", nullable=True
    ),
    Column(
        "type",
        String,
        comment="The type of the file returned (e.g., `csv`, `pdf`, `jpg`, or `png`)",
        nullable=True,
    ),
    Column(
        "url",
        String,
        comment="The URL from which the file can be downloaded using your live secret API key",
        nullable=True,
    ),
)
__all__ = ["file.json"]
