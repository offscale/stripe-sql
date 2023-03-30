from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table, list

from . import metadata

AccountCapabilityRequirements.Json = Table(
    "account_capability_requirements.json",
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
        comment="Date by which the fields in `currently_due` must be collected to keep the capability enabled for the account. These fields may disable the capability sooner if the next threshold is reached before they are collected",
        nullable=True,
    ),
    Column(
        "currently_due",
        ARRAY(String),
        comment="Fields that need to be collected to keep the capability enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the capability is disabled",
    ),
    Column(
        "disabled_reason",
        String,
        comment="If the capability is disabled, this string describes why. Can be `requirements.past_due`, `requirements.pending_verification`, `listed`, `platform_paused`, `rejected.fraud`, `rejected.listed`, `rejected.terms_of_service`, `rejected.other`, `under_review`, or `other`.\n\n`rejected.unsupported_business` means that the account's business is not supported by the capability. For example, payment methods may restrict the businesses they support in their terms of service:\n\n- [Afterpay Clearpay's terms of service](/afterpay-clearpay/legal#restricted-businesses)\n\nIf you believe that the rejection is in error, please contact support at https://support.stripe.com/contact/ for assistance",
        nullable=True,
    ),
    Column(
        "errors",
        list,
        comment="Fields that are `currently_due` and need to be collected again because validation or verification failed",
    ),
    Column(
        "eventually_due",
        ARRAY(String),
        comment="Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set",
    ),
    Column(
        "past_due",
        ARRAY(String),
        comment="Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the capability on the account",
    ),
    Column(
        "pending_verification",
        ARRAY(String),
        comment="Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_capability_requirements.json"]
