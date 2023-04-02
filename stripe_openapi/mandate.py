from sqlalchemy import Boolean, Column, ForeignKey, String, Table

from . import metadata

MandateJson = Table(
    "mandatejson",
    metadata,
    Column("customer_acceptance", CustomerAcceptance, ForeignKey("CustomerAcceptance")),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column("multi_use", MandateMultiUse, ForeignKey("MandateMultiUse"), nullable=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of the payment method associated with this mandate",
    ),
    Column(
        "payment_method_details",
        MandatePaymentMethodDetails,
        ForeignKey("MandatePaymentMethodDetails"),
    ),
    Column(
        "single_use", MandateSingleUse, ForeignKey("MandateSingleUse"), nullable=True
    ),
    Column(
        "status",
        String,
        comment="The status of the mandate, which indicates whether it can be used to initiate a payment",
    ),
    Column("type", String, comment="The type of the mandate"),
)
__all__ = ["mandate.json"]
