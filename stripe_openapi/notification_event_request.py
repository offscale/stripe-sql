from sqlalchemy import Column, String

from . import Base


class NotificationEventRequest(Base):
    __tablename__ = "notification_event_request"
    id = Column(
        String,
        comment="ID of the API request that caused the event. If null, the event was automatic (e.g., Stripe's automatic subscription handling). Request logs are available in the [dashboard](https://dashboard.stripe.com/logs), but currently not in the API",
        nullable=True,
        primary_key=True,
    )
    idempotency_key = Column(
        String,
        comment="The idempotency key transmitted during the request, if any. *Note: This property is populated only for events on or after May 23, 2017*",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "NotificationEventRequest(id={id!r}, idempotency_key={idempotency_key!r})".format(
            id=self.id, idempotency_key=self.idempotency_key
        )


__all__ = ["notification_event_request"]
