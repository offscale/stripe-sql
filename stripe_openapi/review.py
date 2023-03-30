from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.charge import Charge

from . import metadata

Review.Json = Table(
    "review.json",
    metadata,
    Column(
        "billing_zip",
        String,
        comment="The ZIP or postal code of the card used, if applicable",
        nullable=True,
    ),
    Column(
        "charge",
        Charge,
        ForeignKey("Charge"),
        comment="The charge associated with this review",
        nullable=True,
    ),
    Column(
        "closed_reason",
        String,
        comment="The reason the review was closed, or null if it has not yet been closed. One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "ip_address",
        String,
        comment="The IP address where the payment originated",
        nullable=True,
    ),
    Column(
        "ip_address_location",
        RadarReviewResourceLocation,
        ForeignKey("RadarReviewResourceLocation"),
        comment="Information related to the location of the payment. Note that this information is an approximation and attempts to locate the nearest population center - it should not be used to determine a specific address",
        nullable=True,
    ),
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
    Column("open", Boolean, comment="If `true`, the review needs action"),
    Column(
        "opened_reason",
        String,
        comment="The reason the review was opened. One of `rule` or `manual`",
    ),
    Column(
        "payment_intent",
        PaymentIntent,
        ForeignKey("PaymentIntent"),
        comment="The PaymentIntent ID associated with this review, if one exists",
        nullable=True,
    ),
    Column(
        "reason",
        String,
        comment="The reason the review is currently open or closed. One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`",
    ),
    Column(
        "session",
        RadarReviewResourceSession,
        ForeignKey("RadarReviewResourceSession"),
        comment="Information related to the browsing session of the user who initiated the payment",
        nullable=True,
    ),
)
__all__ = ["review.json"]
