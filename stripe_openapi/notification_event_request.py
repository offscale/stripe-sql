from sqlalchemy import Column, String, Table

from . import metadata

NotificationEventRequestJson = Table(
    "notification_event_requestjson",
    metadata,
    Column(
        "id",
        String,
        comment="ID of the API request that caused the event. If null, the event was automatic (e.g., Stripe's automatic subscription handling). Request logs are available in the [dashboard](https://dashboard.stripe.com/logs), but currently not in the API",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "idempotency_key",
        String,
        comment="The idempotency key transmitted during the request, if any. *Note: This property is populated only for events on or after May 23, 2017*",
        nullable=True,
    ),
)
__all__ = ["notification_event_request.json"]
