from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

ScheduledQueryRun.Json = Table(
    "scheduled_query_run.json",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "data_load_time",
        Integer,
        comment="When the query was run, Sigma contained a snapshot of your Stripe data at this time",
    ),
    Column(
        "error",
        SigmaScheduledQueryRunError,
        ForeignKey("SigmaScheduledQueryRunError"),
        nullable=True,
    ),
    Column(
        "file",
        File,
        ForeignKey("File"),
        comment="The file object representing the results of the query",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "result_available_until",
        Integer,
        comment="Time at which the result expires and is no longer available for download",
    ),
    Column("sql", String, comment="SQL for the query"),
    Column(
        "status",
        String,
        comment="The query's execution status, which will be `completed` for successful runs, and `canceled`, `failed`, or `timed_out` otherwise",
    ),
    Column("title", String, comment="Title of the query"),
)
__all__ = ["scheduled_query_run.json"]
