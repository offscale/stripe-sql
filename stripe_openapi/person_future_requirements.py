from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table, list

from . import metadata

PersonFutureRequirements.Json = Table(
    "person_future_requirements.json",
    metadata,
    Column(
        "alternatives",
        list,
        comment="Fields that are due and can be satisfied by providing the corresponding alternative fields instead",
        nullable=True,
    ),
    Column(
        "currently_due",
        ARRAY(String),
        comment="Fields that need to be collected to keep the person's account enabled. If not collected by the account's `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash, and may immediately become `past_due`, but the account may also be given a grace period depending on the account's enablement state prior to transition",
    ),
    Column(
        "errors",
        list,
        comment="Fields that are `currently_due` and need to be collected again because validation or verification failed",
    ),
    Column(
        "eventually_due",
        ARRAY(String),
        comment="Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and the account's `future_requirements[current_deadline]` becomes set",
    ),
    Column(
        "past_due",
        ARRAY(String),
        comment="Fields that weren't collected by the account's `requirements.current_deadline`. These fields need to be collected to enable the person's account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`",
    ),
    Column(
        "pending_verification",
        ARRAY(String),
        comment="Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["person_future_requirements.json"]
