from sqlalchemy import Boolean, Column, Integer, String


class Portal_Subscription_Update(Base):
    __tablename__ = "portal_subscription_update"
    default_allowed_updates = Column(
        ARRAY(String),
        comment="The types of subscription updates that are supported for items listed in the `products` attribute. When empty, subscriptions are not updateable",
    )
    enabled = Column(Boolean, comment="Whether the feature is enabled")
    products = Column(
        list,
        comment="The list of products that support subscription updates",
        nullable=True,
    )
    proration_behavior = Column(
        String,
        comment="Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Portal_Subscription_Update(default_allowed_updates={default_allowed_updates!r}, enabled={enabled!r}, products={products!r}, proration_behavior={proration_behavior!r}, id={id!r})".format(
            default_allowed_updates=self.default_allowed_updates,
            enabled=self.enabled,
            products=self.products,
            proration_behavior=self.proration_behavior,
            id=self.id,
        )


__all__ = ["portal_subscription_update"]
