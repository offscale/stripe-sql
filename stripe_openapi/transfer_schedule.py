from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TransferScheduleJson = Table(
    "transfer_schedulejson",
    metadata,
    Column(
        "delay_days",
        Integer,
        comment="The number of days charges for the account will be held before being paid out",
    ),
    Column(
        "interval",
        String,
        comment="How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`",
    ),
    Column(
        "monthly_anchor",
        Integer,
        comment="The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months",
        nullable=True,
    ),
    Column(
        "weekly_anchor",
        String,
        comment="The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["transfer_schedule.json"]
