from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

GelatoSessionIdNumberOptions.Json = Table(
    "gelato_session_id_number_options.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_session_id_number_options.json"]
