from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from . import metadata

EventJson = Table(
    "eventjson",
    metadata,
    Column(
        "account",
        String,
        comment="The connected account that originated the event",
        nullable=True,
    ),
    Column(
        "api_version",
        String,
        comment="The Stripe API version used to render `data`. *Note: This property is populated only for events on or after October 31, 2014*",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("data", NotificationEventData, ForeignKey("NotificationEventData")),
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
        "pending_webhooks",
        Integer,
        comment="Number of webhooks that have yet to be successfully delivered (i.e., to return a 20x response) to the URLs you've specified",
    ),
    Column(
        "request",
        NotificationEventRequest,
        ForeignKey("NotificationEventRequest"),
        comment="Information on the API request that instigated the event",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Description of the event (e.g., `invoice.created` or `charge.refunded`)",
    ),
)
__all__ = ["event.json"]
