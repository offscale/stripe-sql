from sqlalchemy import ARRAY, JSON, Boolean, Column, Integer, String, Table

from . import metadata

WebhookEndpointJson = Table(
    "webhook_endpointjson",
    metadata,
    Column(
        "api_version",
        String,
        comment="The API version events are rendered as for this webhook endpoint",
        nullable=True,
    ),
    Column(
        "application",
        String,
        comment="The ID of the associated Connect application",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "description",
        String,
        comment="An optional description of what the webhook is used for",
        nullable=True,
    ),
    Column(
        "enabled_events",
        ARRAY(String),
        comment="The list of events to enable for this endpoint. `['*']` indicates that all events are enabled, except those that require explicit selection",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "secret",
        String,
        comment="The endpoint's secret, used to generate [webhook signatures](https://stripe.com/docs/webhooks/signatures). Only returned at creation",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The status of the webhook. It can be `enabled` or `disabled`",
    ),
    Column("url", String, comment="The URL of the webhook endpoint"),
)
__all__ = ["webhook_endpoint.json"]
