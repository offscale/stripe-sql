from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

SchedulesPhaseAutomaticTaxJson = Table(
    "schedules_phase_automatic_taxjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Whether Stripe automatically computes tax on invoices created during this phase",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["schedules_phase_automatic_tax.json"]
