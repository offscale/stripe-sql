from sqlalchemy import Column, Integer, String


class Payment_Links_Resource_Subscription_Data(Base):
    __tablename__ = "payment_links_resource_subscription_data"
    description = Column(
        String,
        comment="The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    )
    trial_period_days = Column(
        Integer,
        comment="Integer representing the number of trial period days before the customer is charged for the first time",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Links_Resource_Subscription_Data(description={description!r}, trial_period_days={trial_period_days!r}, id={id!r})".format(
            description=self.description,
            trial_period_days=self.trial_period_days,
            id=self.id,
        )


__all__ = ["payment_links_resource_subscription_data"]
