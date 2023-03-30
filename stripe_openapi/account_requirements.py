from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table, list

from . import metadata

AccountRequirements.Json = Table(
    "account_requirements.json",
    metadata,
    Column(
        "alternatives",
        list,
        comment="Fields that are due and can be satisfied by providing the corresponding alternative fields instead",
        nullable=True,
    ),
    Column(
        "current_deadline",
        Integer,
        comment="Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected",
        nullable=True,
    ),
    Column(
        "currently_due",
        ARRAY(String),
        comment="Fields that need to be collected to keep the account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled",
        nullable=True,
    ),
    Column(
        "disabled_reason",
        String,
        comment="If the account is disabled, this string describes why. Can be `requirements.past_due`, `requirements.pending_verification`, `listed`, `platform_paused`, `rejected.fraud`, `rejected.listed`, `rejected.terms_of_service`, `rejected.other`, `under_review`, or `other`",
        nullable=True,
    ),
    Column(
        "errors",
        list,
        comment="Fields that are `currently_due` and need to be collected again because validation or verification failed",
        nullable=True,
    ),
    Column(
        "eventually_due",
        ARRAY(String),
        comment="Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set",
        nullable=True,
    ),
    Column(
        "past_due",
        ARRAY(String),
        comment="Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the account",
        nullable=True,
    ),
    Column(
        "pending_verification",
        ARRAY(String),
        comment="Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_requirements.json"]
