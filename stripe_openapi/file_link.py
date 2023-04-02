from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

FileLinkJson = Table(
    "file_linkjson",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("expired", Boolean, comment="Whether this link is already expired"),
    Column(
        "expires_at", Integer, comment="Time at which the link expires", nullable=True
    ),
    Column(
        "file", File, ForeignKey("File"), comment="The file object this link points to"
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "url",
        String,
        comment="The publicly accessible URL to download the file",
        nullable=True,
    ),
)
__all__ = ["file_link.json"]
