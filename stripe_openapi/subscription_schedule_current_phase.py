from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SubscriptionScheduleCurrentPhaseJson = Table(
    "subscription_schedule_current_phasejson",
    metadata,
    Column(
        "end_date",
        Integer,
        comment="The end of this phase of the subscription schedule",
    ),
    Column(
        "start_date",
        Integer,
        comment="The start of this phase of the subscription schedule",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedule_current_phase.json"]
