from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from . import Base


class Event(Base):
    """
    Events are our way of letting you know when something interesting happens in

    your account. When an interesting event occurs, we create a new `Event`
    object. For example, when a charge succeeds, we create a `charge.succeeded`
    event; and when an invoice payment attempt fails, we create an
    `invoice.payment_failed` event. Note that many API requests may cause multiple
    events to be created. For example, if you create a new subscription for a
    customer, you will receive both a `customer.subscription.created` event and a
    `charge.succeeded` event.

    Events occur when the state of another API resource changes. The state of that
    resource at the time of the change is embedded in the event's data field. For
    example, a `charge.succeeded` event will contain a charge, and an
    `invoice.payment_failed` event will contain an invoice.

    As with other API resources, you can use endpoints to retrieve an
    [individual event](https://stripe.com/docs/api#retrieve_event) or a [list of events](https://stripe.com/docs/api#list_events)
    from the API. We also have a separate
    [webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the
    `Event` objects directly to an endpoint on your server. Webhooks are managed
    in your
    [account settings](https://dashboard.stripe.com/account/webhooks),
    and our [Using Webhooks](https://stripe.com/docs/webhooks) guide will help you get set up.

    When using [Connect](https://stripe.com/docs/connect), you can also receive notifications of
    events that occur in connected accounts. For these events, there will be an
    additional `account` attribute in the received `Event` object.

    **NOTE:** Right now, access to events through the [Retrieve Event API](https://stripe.com/docs/api#retrieve_event) is
    guaranteed only for 30 days.

    """

    __tablename__ = "event"
    account = Column(
        String, comment="The connected account that originated the event", nullable=True
    )
    api_version = Column(
        String,
        comment="The Stripe API version used to render `data`. *Note: This property is populated only for events on or after October 31, 2014*",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    data = Column(Integer, ForeignKey("notification_event_data.id"))
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    pending_webhooks = Column(
        Integer,
        comment="Number of webhooks that have yet to be successfully delivered (i.e., to return a 20x response) to the URLs you've specified",
    )
    request = Column(
        String,
        ForeignKey("notification_event_request.id"),
        comment="Information on the API request that instigated the event",
        nullable=True,
    )
    type = Column(
        String,
        comment="Description of the event (e.g., `invoice.created` or `charge.refunded`)",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Event(account={account!r}, api_version={api_version!r}, created={created!r}, data={data!r}, id={id!r}, livemode={livemode!r}, object={object!r}, pending_webhooks={pending_webhooks!r}, request={request!r}, type={type!r})".format(
            account=self.account,
            api_version=self.api_version,
            created=self.created,
            data=self.data,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            pending_webhooks=self.pending_webhooks,
            request=self.request,
            type=self.type,
        )


__all__ = ["event"]
