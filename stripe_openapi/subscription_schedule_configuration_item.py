from sqlalchemy import Column, Integer

class Subscription_Schedule_Configuration_Item(Base):
    """
    A phase item describes the price and quantity of a phase.
        """
    __tablename__ = 'subscription_schedule_configuration_item'
    billing_thresholds = Column(SubscriptionItemBillingThresholds, comment='Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period', nullable=True)
    metadata = Column(JSON, comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered", nullable=True)
    plan = Column(string | Plan, comment='ID of the plan to which the customer should be subscribed')
    price = Column(string | Price, comment='ID of the price to which the customer should be subscribed')
    quantity = Column(Integer, comment='Quantity of the plan to which the customer should be subscribed', nullable=True)
    tax_rates = Column(list, comment='The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Subscription_Schedule_Configuration_Item(billing_thresholds={billing_thresholds!r}, metadata={metadata!r}, plan={plan!r}, price={price!r}, quantity={quantity!r}, tax_rates={tax_rates!r}, id={id!r})'.format(billing_thresholds=self.billing_thresholds, metadata=self.metadata, plan=self.plan, price=self.price, quantity=self.quantity, tax_rates=self.tax_rates, id=self.id)
__all__ = ['subscription_schedule_configuration_item']