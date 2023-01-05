from sqlalchemy import Boolean, Column, Integer, String


class Webhook_Endpoint(Base):
    """
    You can configure [webhook endpoints](https://stripe.com/docs/webhooks/) via the API to be

    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up Webhooks](https://stripe.com/docs/webhooks/configure).

    """

    __tablename__ = "webhook_endpoint"
    api_version = Column(
        String,
        comment="The API version events are rendered as for this webhook endpoint",
        nullable=True,
    )
    application = Column(
        String, comment="The ID of the associated Connect application", nullable=True
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    description = Column(
        String,
        comment="An optional description of what the webhook is used for",
        nullable=True,
    )
    enabled_events = Column(
        ARRAY(String),
        comment="The list of events to enable for this endpoint. `['*']` indicates that all events are enabled, except those that require explicit selection",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    secret = Column(
        String,
        comment="The endpoint's secret, used to generate [webhook signatures](https://stripe.com/docs/webhooks/signatures). Only returned at creation",
        nullable=True,
    )
    status = Column(
        String, comment="The status of the webhook. It can be `enabled` or `disabled`"
    )
    url = Column(String, comment="The URL of the webhook endpoint")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Webhook_Endpoint(api_version={api_version!r}, application={application!r}, created={created!r}, description={description!r}, enabled_events={enabled_events!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, secret={secret!r}, status={status!r}, url={url!r})".format(
            api_version=self.api_version,
            application=self.application,
            created=self.created,
            description=self.description,
            enabled_events=self.enabled_events,
            id=self.id,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            secret=self.secret,
            status=self.status,
            url=self.url,
        )


__all__ = ["webhook_endpoint"]
