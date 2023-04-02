from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.charge import Charge

from . import metadata

DisputeJson = Table(
    "disputejson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Disputed amount. Usually the amount of the charge, but can differ (usually because of currency fluctuation or because only part of the order is disputed)",
    ),
    Column(
        "balance_transactions",
        list,
        comment="List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute",
    ),
    Column(
        "charge",
        Charge,
        ForeignKey("Charge"),
        comment="ID of the charge that was disputed",
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column("evidence", DisputeEvidence, ForeignKey("DisputeEvidence")),
    Column(
        "evidence_details", DisputeEvidenceDetails, ForeignKey("DisputeEvidenceDetails")
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "is_charge_refundable",
        Boolean,
        comment="If true, it is still possible to refund the disputed payment. Once the payment has been fully refunded, no further funds will be withdrawn from your Stripe account as a result of this dispute",
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "network_reason_code",
        String,
        comment="Network-dependent reason code for the dispute",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "payment_intent",
        PaymentIntent,
        ForeignKey("PaymentIntent"),
        comment="ID of the PaymentIntent that was disputed",
        nullable=True,
    ),
    Column(
        "reason",
        String,
        comment="Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Read more about [dispute reasons](https://stripe.com/docs/disputes/categories)",
    ),
    Column(
        "status",
        String,
        comment="Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `charge_refunded`, `won`, or `lost`",
    ),
)
__all__ = ["dispute.json"]
