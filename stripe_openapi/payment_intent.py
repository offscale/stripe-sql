from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.application import Application
from stripe_openapi.charge import Charge
from stripe_openapi.customer import Customer
from stripe_openapi.invoice import Invoice
from stripe_openapi.review import Review
from stripe_openapi.shipping import Shipping

from . import metadata

PaymentIntentJson = Table(
    "payment_intentjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)",
    ),
    Column(
        "amount_capturable",
        Integer,
        comment="Amount that can be captured from this PaymentIntent",
    ),
    Column(
        "amount_details",
        PaymentFlowsAmountDetails,
        ForeignKey("PaymentFlowsAmountDetails"),
        nullable=True,
    ),
    Column(
        "amount_received",
        Integer,
        comment="Amount that was collected by this PaymentIntent",
    ),
    Column(
        "application",
        Application,
        ForeignKey("Application"),
        comment="ID of the Connect application that created the PaymentIntent",
        nullable=True,
    ),
    Column(
        "application_fee_amount",
        Integer,
        comment="The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total payment amount. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)",
        nullable=True,
    ),
    Column(
        "automatic_payment_methods",
        PaymentFlowsAutomaticPaymentMethodsPaymentIntent,
        ForeignKey("PaymentFlowsAutomaticPaymentMethodsPaymentIntent"),
        comment="Settings to configure compatible payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)",
        nullable=True,
    ),
    Column(
        "canceled_at",
        Integer,
        comment="Populated when `status` is `canceled`, this is the time at which the PaymentIntent was canceled. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "cancellation_reason",
        String,
        comment="Reason for cancellation of this PaymentIntent, either user-provided (`duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`) or generated by Stripe internally (`failed_invoice`, `void_invoice`, or `automatic`)",
        nullable=True,
    ),
    Column(
        "capture_method",
        String,
        comment="Controls when the funds will be captured from the customer's account",
    ),
    Column(
        "client_secret",
        String,
        comment="The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key. \n\nThe client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.\n\nRefer to our docs to [accept a payment](https://stripe.com/docs/payments/accept-a-payment?ui=elements) and learn about how `client_secret` should be handled",
        nullable=True,
    ),
    Column("confirmation_method", String),
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
        comment="ID of the Customer this PaymentIntent belongs to, if one exists.\n\nPayment methods attached to other Customers cannot be used with this PaymentIntent.\n\nIf present in combination with [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage), this PaymentIntent's payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        Invoice,
        ForeignKey("Invoice"),
        comment="ID of the invoice that created this PaymentIntent, if it exists",
        nullable=True,
    ),
    Column(
        "last_payment_error",
        ApiErrors,
        ForeignKey("ApiErrors"),
        comment="The payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason",
        nullable=True,
    ),
    Column(
        "latest_charge",
        Charge,
        ForeignKey("Charge"),
        comment="The latest charge created by this payment intent",
        nullable=True,
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. For more information, see the [documentation](https://stripe.com/docs/payments/payment-intents/creating-payment-intents#storing-information-in-metadata)",
    ),
    Column(
        "next_action",
        PaymentIntentNextAction,
        ForeignKey("PaymentIntentNextAction"),
        comment="If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source",
        nullable=True,
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
        comment="The account (if any) for which the funds of the PaymentIntent are intended. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts) for details",
        nullable=True,
    ),
    Column(
        "payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of the payment method used in this PaymentIntent",
        nullable=True,
    ),
    Column(
        "payment_method_options",
        PaymentIntentPaymentMethodOptions,
        ForeignKey("PaymentIntentPaymentMethodOptions"),
        comment="Payment-method-specific configuration for this PaymentIntent",
        nullable=True,
    ),
    Column(
        "payment_method_types",
        ARRAY(String),
        comment="The list of payment method types (e.g. card) that this PaymentIntent is allowed to use",
    ),
    Column(
        "processing",
        PaymentIntentProcessing,
        ForeignKey("PaymentIntentProcessing"),
        comment="If present, this property tells you about the processing state of the payment",
        nullable=True,
    ),
    Column(
        "receipt_email",
        String,
        comment="Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails)",
        nullable=True,
    ),
    Column(
        "review",
        Review,
        ForeignKey("Review"),
        comment="ID of the review associated with this PaymentIntent, if any",
        nullable=True,
    ),
    Column(
        "setup_future_usage",
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    ),
    Column(
        "shipping",
        Shipping,
        ForeignKey("Shipping"),
        comment="Shipping information for this PaymentIntent",
        nullable=True,
    ),
    Column(
        "source",
        PaymentSource,
        ForeignKey("DeletedPaymentSource"),
        comment="This is a legacy field that will be removed in the future. It is the ID of the Source object that is associated with this PaymentIntent, if one was supplied",
        nullable=True,
    ),
    Column(
        "statement_descriptor",
        String,
        comment="For non-card charges, you can use this value as the complete description that appears on your customers’ statements. Must contain at least one letter, maximum 22 characters",
        nullable=True,
    ),
    Column(
        "statement_descriptor_suffix",
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="Status of this PaymentIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `requires_capture`, `canceled`, or `succeeded`. Read more about each PaymentIntent [status](https://stripe.com/docs/payments/intents#intent-statuses)",
    ),
    Column(
        "transfer_data",
        TransferData,
        ForeignKey("TransferData"),
        comment="The data with which to automatically create a Transfer when the payment is finalized. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts) for details",
        nullable=True,
    ),
    Column(
        "transfer_group",
        String,
        comment="A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts) for details",
        nullable=True,
    ),
)
__all__ = ["payment_intent.json"]
