from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.application import Application
from stripe_openapi.customer import Customer
from stripe_openapi.subscription import Subscription

from . import metadata

SubscriptionSchedule.Json = Table(
    "subscription_schedule.json",
    metadata,
    Column(
        "application",
        Application,
        ForeignKey("DeletedApplication"),
        comment="ID of the Connect Application that created the schedule",
        nullable=True,
    ),
    Column(
        "canceled_at",
        Integer,
        comment="Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "completed_at",
        Integer,
        comment="Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "current_phase",
        SubscriptionScheduleCurrentPhase,
        ForeignKey("SubscriptionScheduleCurrentPhase"),
        comment="Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`",
        nullable=True,
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="ID of the customer who owns the subscription schedule",
    ),
    Column(
        "default_settings",
        SubscriptionSchedulesResourceDefaultSettings,
        ForeignKey("SubscriptionSchedulesResourceDefaultSettings"),
    ),
    Column(
        "end_behavior",
        String,
        comment="Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running.`cancel` will end the subscription schedule and cancel the underlying subscription",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "phases", list, comment="Configuration for the subscription schedule's phases"
    ),
    Column(
        "released_at",
        Integer,
        comment="Time at which the subscription schedule was released. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "released_subscription",
        String,
        comment="ID of the subscription once managed by the subscription schedule (if it is released)",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules)",
    ),
    Column(
        "subscription",
        Subscription,
        ForeignKey("Subscription"),
        comment="ID of the subscription managed by the subscription schedule",
        nullable=True,
    ),
    Column(
        "test_clock",
        Test_Helpers__TestClock,
        ForeignKey("Test_Helpers__TestClock"),
        comment="ID of the test clock this subscription schedule belongs to",
        nullable=True,
    ),
)
__all__ = ["subscription_schedule.json"]
