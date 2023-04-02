from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SubscriptionsResourcePauseCollectionJson = Table(
    "subscriptions_resource_pause_collectionjson",
    metadata,
    Column(
        "behavior",
        String,
        comment="The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`",
    ),
    Column(
        "resumes_at",
        Integer,
        comment="The time after which the subscription will resume collecting payments",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscriptions_resource_pause_collection.json"]
