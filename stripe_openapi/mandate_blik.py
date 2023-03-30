from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

MandateBlik.Json = Table(
    "mandate_blik.json",
    metadata,
    Column(
        "expires_after",
        Integer,
        comment="Date at which the mandate expires",
        nullable=True,
    ),
    Column(
        "off_session",
        MandateOptionsOffSessionDetailsBlik,
        ForeignKey("MandateOptionsOffSessionDetailsBlik"),
        nullable=True,
    ),
    Column("type", String, comment="Type of the mandate", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_blik.json"]
