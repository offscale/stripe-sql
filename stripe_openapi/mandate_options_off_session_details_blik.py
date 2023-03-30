from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

MandateOptionsOffSessionDetailsBlik.Json = Table(
    "mandate_options_off_session_details_blik.json",
    metadata,
    Column(
        "amount", Integer, comment="Amount of each recurring payment", nullable=True
    ),
    Column(
        "currency", String, comment="Currency of each recurring payment", nullable=True
    ),
    Column(
        "interval",
        String,
        comment="Frequency interval of each recurring payment",
        nullable=True,
    ),
    Column(
        "interval_count",
        Integer,
        comment="Frequency indicator of each recurring payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_options_off_session_details_blik.json"]
