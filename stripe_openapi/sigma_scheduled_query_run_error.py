from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SigmaScheduledQueryRunErrorJson = Table(
    "sigma_scheduled_query_run_errorjson",
    metadata,
    Column("message", String, comment="Information about the run failure"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["sigma_scheduled_query_run_error.json"]
