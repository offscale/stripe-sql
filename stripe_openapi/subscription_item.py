from sqlalchemy import Column, Integer, String


class Subscription_Item(Base):
    """
    Subscription items allow you to create customer subscriptions with more than

    one plan, making it easy to represent complex billing relationships.

    """

    __tablename__ = "subscription_item"
    billing_thresholds = Column(
        subscription_item_billing_thresholds,
        comment="[[FK(subscription_item_billing_thresholds)]] Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    plan = Column(plan, ForeignKey("plan"))
    price = Column(price, ForeignKey("price"))
    quantity = Column(
        Integer,
        comment="The [quantity](https://stripe.com/docs/subscriptions/quantities) of the plan to which the customer should be subscribed",
        nullable=True,
    )
    subscription = Column(
        String, comment="The `subscription` this `subscription_item` belongs to"
    )
    tax_rates = Column(
        list,
        comment="The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Item(billing_thresholds={billing_thresholds!r}, created={created!r}, id={id!r}, metadata={metadata!r}, object={object!r}, plan={plan!r}, price={price!r}, quantity={quantity!r}, subscription={subscription!r}, tax_rates={tax_rates!r})".format(
            billing_thresholds=self.billing_thresholds,
            created=self.created,
            id=self.id,
            metadata=self.metadata,
            object=self.object,
            plan=self.plan,
            price=self.price,
            quantity=self.quantity,
            subscription=self.subscription,
            tax_rates=self.tax_rates,
        )


__all__ = ["subscription_item"]
