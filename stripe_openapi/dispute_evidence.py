from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

DisputeEvidence.Json = Table(
    "dispute_evidence.json",
    metadata,
    Column(
        "access_activity_log",
        String,
        comment="Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity",
        nullable=True,
    ),
    Column(
        "billing_address",
        String,
        comment="The billing address provided by the customer",
        nullable=True,
    ),
    Column(
        "cancellation_policy",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer",
        nullable=True,
    ),
    Column(
        "cancellation_policy_disclosure",
        String,
        comment="An explanation of how and when the customer was shown your refund policy prior to purchase",
        nullable=True,
    ),
    Column(
        "cancellation_rebuttal",
        String,
        comment="A justification for why the customer's subscription was not canceled",
        nullable=True,
    ),
    Column(
        "customer_communication",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service",
        nullable=True,
    ),
    Column(
        "customer_email_address",
        String,
        comment="The email address of the customer",
        nullable=True,
    ),
    Column("customer_name", String, comment="The name of the customer", nullable=True),
    Column(
        "customer_purchase_ip",
        String,
        comment="The IP address that the customer used when making the purchase",
        nullable=True,
    ),
    Column(
        "customer_signature",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer's signature",
        nullable=True,
    ),
    Column(
        "duplicate_charge_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate",
        nullable=True,
    ),
    Column(
        "duplicate_charge_explanation",
        String,
        comment="An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate",
        nullable=True,
    ),
    Column(
        "duplicate_charge_id",
        String,
        comment="The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge",
        nullable=True,
    ),
    Column(
        "product_description",
        String,
        comment="A description of the product or service that was sold",
        nullable=True,
    ),
    Column(
        "receipt",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge",
        nullable=True,
    ),
    Column(
        "refund_policy",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer",
        nullable=True,
    ),
    Column(
        "refund_policy_disclosure",
        String,
        comment="Documentation demonstrating that the customer was shown your refund policy prior to purchase",
        nullable=True,
    ),
    Column(
        "refund_refusal_explanation",
        String,
        comment="A justification for why the customer is not entitled to a refund",
        nullable=True,
    ),
    Column(
        "service_date",
        String,
        comment="The date on which the customer received or began receiving the purchased service, in a clear human-readable format",
        nullable=True,
    ),
    Column(
        "service_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement",
        nullable=True,
    ),
    Column(
        "shipping_address",
        String,
        comment="The address to which a physical product was shipped. You should try to include as complete address information as possible",
        nullable=True,
    ),
    Column(
        "shipping_carrier",
        String,
        comment="The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas",
        nullable=True,
    ),
    Column(
        "shipping_date",
        String,
        comment="The date on which a physical product began its route to the shipping address, in a clear human-readable format",
        nullable=True,
    ),
    Column(
        "shipping_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer's full shipping address, if possible",
        nullable=True,
    ),
    Column(
        "shipping_tracking_number",
        String,
        comment="The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas",
        nullable=True,
    ),
    Column(
        "uncategorized_file",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements",
        nullable=True,
    ),
    Column(
        "uncategorized_text",
        String,
        comment="Any additional evidence or statements",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["dispute_evidence.json"]
