from sqlalchemy import Boolean, Column, Integer, String

class Subscription_Schedule(Base):
    """
        A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.
    
        Related guide: [Subscription Schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules).
    
        """
    __tablename__ = 'subscription_schedule'
    application = Column(string | Application, comment='ID of the Connect Application that created the schedule', nullable=True)
    canceled_at = Column(Integer, comment='Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch', nullable=True)
    completed_at = Column(Integer, comment='Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch', nullable=True)
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    current_phase = Column(SubscriptionScheduleCurrentPhase, comment='Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`', nullable=True)
    customer = Column(string | Customer, comment='ID of the customer who owns the subscription schedule')
    default_settings = Column(SubscriptionSchedulesResourceDefaultSettings)
    end_behavior = Column(String, comment='Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running.`cancel` will end the subscription schedule and cancel the underlying subscription')
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format', nullable=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    phases = Column(list, comment="Configuration for the subscription schedule's phases")
    released_at = Column(Integer, comment='Time at which the subscription schedule was released. Measured in seconds since the Unix epoch', nullable=True)
    released_subscription = Column(String, comment='ID of the subscription once managed by the subscription schedule (if it is released)', nullable=True)
    status = Column(String, comment='The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules)')
    subscription = Column(Subscription, comment='ID of the subscription managed by the subscription schedule', nullable=True)
    test_clock = Column(TestHelpers.TestClock, comment='ID of the test clock this subscription schedule belongs to', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Subscription_Schedule(application={application!r}, canceled_at={canceled_at!r}, completed_at={completed_at!r}, created={created!r}, current_phase={current_phase!r}, customer={customer!r}, default_settings={default_settings!r}, end_behavior={end_behavior!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, phases={phases!r}, released_at={released_at!r}, released_subscription={released_subscription!r}, status={status!r}, subscription={subscription!r}, test_clock={test_clock!r})'.format(application=self.application, canceled_at=self.canceled_at, completed_at=self.completed_at, created=self.created, current_phase=self.current_phase, customer=self.customer, default_settings=self.default_settings, end_behavior=self.end_behavior, id=self.id, livemode=self.livemode, metadata=self.metadata, object=self.object, phases=self.phases, released_at=self.released_at, released_subscription=self.released_subscription, status=self.status, subscription=self.subscription, test_clock=self.test_clock)
__all__ = ['subscription_schedule']