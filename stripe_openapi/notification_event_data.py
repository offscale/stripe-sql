from sqlalchemy import JSON, Column, Identity, Integer, Table

from . import metadata

NotificationEventDataJson = Table(
    "notification_event_datajson",
    metadata,
    Column(
        "object",
        JSON,
        comment="Object containing the API resource relevant to the event. For example, an `invoice.created` event will have a full [invoice object](https://stripe.com/docs/api#invoice_object) as the value of the object key",
    ),
    Column(
        "previous_attributes",
        JSON,
        comment="Object containing the names of the attributes that have changed, and their previous values (sent along only with *.updated events)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["notification_event_data.json"]
