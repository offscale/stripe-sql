from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.application import Application
from stripe_openapi.customer import Customer
from stripe_openapi.dispute import Dispute
from stripe_openapi.invoice import Invoice
from stripe_openapi.level3 import Level3
from stripe_openapi.review import Review
from stripe_openapi.shipping import Shipping
from stripe_openapi.transfer import Transfer

from . import metadata

Charge.Json = Table(
    "charge.json",
    metadata,
    Column(
        "alternate_statement_descriptors",
        AlternateStatementDescriptors,
        ForeignKey("AlternateStatementDescriptors"),
        nullable=True,
    ),
    Column(
        "amount",
        Integer,
        comment="Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)",
    ),
    Column(
        "amount_captured",
        Integer,
        comment="Amount in %s captured (can be less than the amount attribute on the charge if a partial capture was made)",
    ),
    Column(
        "amount_refunded",
        Integer,
        comment="Amount in %s refunded (can be less than the amount attribute on the charge if a partial refund was issued)",
    ),
    Column(
        "application",
        Application,
        ForeignKey("Application"),
        comment="ID of the Connect application that created the charge",
        nullable=True,
    ),
    Column(
        "application_fee",
        ApplicationFee,
        ForeignKey("ApplicationFee"),
        comment="The application fee (if any) for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details",
        nullable=True,
    ),
    Column(
        "application_fee_amount",
        Integer,
        comment="The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details",
        nullable=True,
    ),
    Column(
        "authorization_code",
        String,
        comment="Authorization code on the charge",
        nullable=True,
    ),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes)",
        nullable=True,
    ),
    Column("billing_details", BillingDetails, ForeignKey("BillingDetails")),
    Column(
        "calculated_statement_descriptor",
        String,
        comment="The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined",
        nullable=True,
    ),
    Column(
        "captured",
        Boolean,
        comment="If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured",
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
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="ID of the customer this charge is for if one exists",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request",
        nullable=True,
    ),
    Column(
        "dispute",
        Dispute,
        ForeignKey("Dispute"),
        comment="Details about the dispute if the charge has been disputed",
        nullable=True,
    ),
    Column("disputed", Boolean, comment="Whether the charge has been disputed"),
    Column(
        "failure_balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="ID of the balance transaction that describes the reversal of the balance on your account due to payment failure",
        nullable=True,
    ),
    Column(
        "failure_code",
        String,
        comment="Error code explaining reason for charge failure if available (see [the errors section](https://stripe.com/docs/error-codes) for a list of codes)",
        nullable=True,
    ),
    Column(
        "failure_message",
        String,
        comment="Message to user further explaining reason for charge failure if available",
        nullable=True,
    ),
    Column(
        "fraud_details",
        ChargeFraudDetails,
        ForeignKey("ChargeFraudDetails"),
        comment="Information on fraud assessments for the charge",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        Invoice,
        ForeignKey("Invoice"),
        comment="ID of the invoice this charge is for if one exists",
        nullable=True,
    ),
    Column("level3", Level3, ForeignKey("Level3"), nullable=True),
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
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "on_behalf_of",
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers) for details",
        nullable=True,
    ),
    Column(
        "outcome",
        ChargeOutcome,
        ForeignKey("ChargeOutcome"),
        comment="Details about whether the payment was accepted, and why. See [understanding declines](https://stripe.com/docs/declines) for details",
        nullable=True,
    ),
    Column(
        "paid",
        Boolean,
        comment="`true` if the charge succeeded, or was successfully authorized for later capture",
    ),
    Column(
        "payment_intent",
        PaymentIntent,
        ForeignKey("PaymentIntent"),
        comment="ID of the PaymentIntent associated with this charge, if one exists",
        nullable=True,
    ),
    Column(
        "payment_method",
        String,
        comment="ID of the payment method used in this charge",
        nullable=True,
    ),
    Column(
        "payment_method_details",
        PaymentMethodDetails,
        ForeignKey("PaymentMethodDetails"),
        comment="Details about the payment method at the time of the transaction",
        nullable=True,
    ),
    Column(
        "radar_options",
        RadarRadarOptions,
        ForeignKey("RadarRadarOptions"),
        nullable=True,
    ),
    Column(
        "receipt_email",
        String,
        comment="This is the email address that the receipt for this charge was sent to",
        nullable=True,
    ),
    Column(
        "receipt_number",
        String,
        comment="This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent",
        nullable=True,
    ),
    Column(
        "receipt_url",
        String,
        comment="This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt",
        nullable=True,
    ),
    Column(
        "refunded",
        Boolean,
        comment="Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false",
    ),
    Column(
        "refunds",
        JSON,
        comment="A list of refunds that have been applied to the charge",
        nullable=True,
    ),
    Column(
        "review",
        Review,
        ForeignKey("Review"),
        comment="ID of the review associated with this charge if one exists",
        nullable=True,
    ),
    Column(
        "shipping",
        Shipping,
        ForeignKey("Shipping"),
        comment="Shipping information for the charge",
        nullable=True,
    ),
    Column(
        "source",
        PaymentSource,
        ForeignKey("PaymentSource"),
        comment="This is a legacy field that will be removed in the future. It contains the Source, Card, or BankAccount object used for the charge. For details about the payment method used for this charge, refer to `payment_method` or `payment_method_details` instead",
        nullable=True,
    ),
    Column(
        "source_transfer",
        Transfer,
        ForeignKey("Transfer"),
        comment="The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details",
        nullable=True,
    ),
    Column(
        "statement_descriptor",
        String,
        comment="For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters",
        nullable=True,
    ),
    Column(
        "statement_descriptor_suffix",
        String,
        comment="Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The status of the payment is either `succeeded`, `pending`, or `failed`",
    ),
    Column(
        "transfer",
        Transfer,
        ForeignKey("Transfer"),
        comment="ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter)",
        nullable=True,
    ),
    Column(
        "transfer_data",
        ChargeTransferData,
        ForeignKey("ChargeTransferData"),
        comment="An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details",
        nullable=True,
    ),
    Column(
        "transfer_group",
        String,
        comment="A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers#transfer-options) for details",
        nullable=True,
    ),
)
__all__ = ["charge.json"]
