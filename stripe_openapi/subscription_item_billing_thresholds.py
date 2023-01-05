from sqlalchemy import Column, Integer


class Subscription_Item_Billing_Thresholds(Base):
    __tablename__ = "subscription_item_billing_thresholds"
    usage_gte = Column(
        Integer,
        comment="Usage threshold that triggers the subscription to create an invoice",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Item_Billing_Thresholds(usage_gte={usage_gte!r}, id={id!r})".format(
            usage_gte=self.usage_gte, id=self.id
        )


__all__ = ["subscription_item_billing_thresholds"]
