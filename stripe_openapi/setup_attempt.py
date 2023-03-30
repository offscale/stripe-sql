from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.application import Application
from stripe_openapi.customer import Customer

from . import metadata

SetupAttempt.Json = Table(
    "setup_attempt.json",
    metadata,
    Column(
        "application",
        Application,
        ForeignKey("Application"),
        comment="The value of [application](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-application) on the SetupIntent at the time of this confirmation",
        nullable=True,
    ),
    Column(
        "attach_to_self",
        Boolean,
        comment="If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The value of [customer](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-customer) on the SetupIntent at the time of this confirmation",
        nullable=True,
    ),
    Column(
        "flow_directions",
        ARRAY(String),
        comment="Indicates the directions of money movement for which this payment method is intended to be used.\n\nInclude `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "on_behalf_of",
        Account,
        ForeignKey("Account"),
        comment="The value of [on_behalf_of](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-on_behalf_of) on the SetupIntent at the time of this confirmation",
        nullable=True,
    ),
    Column(
        "payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of the payment method used with this SetupAttempt",
    ),
    Column(
        "payment_method_details",
        SetupAttemptPaymentMethodDetails,
        ForeignKey("SetupAttemptPaymentMethodDetails"),
    ),
    Column(
        "setup_error",
        ApiErrors,
        ForeignKey("ApiErrors"),
        comment="The error encountered during this attempt to confirm the SetupIntent, if any",
        nullable=True,
    ),
    Column(
        "setup_intent",
        SetupIntent,
        ForeignKey("SetupIntent"),
        comment="ID of the SetupIntent that this attempt belongs to",
    ),
    Column(
        "status",
        String,
        comment="Status of this SetupAttempt, one of `requires_confirmation`, `requires_action`, `processing`, `succeeded`, `failed`, or `abandoned`",
    ),
    Column(
        "usage",
        String,
        comment="The value of [usage](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-usage) on the SetupIntent at the time of this confirmation, one of `off_session` or `on_session`",
    ),
)
__all__ = ["setup_attempt.json"]
