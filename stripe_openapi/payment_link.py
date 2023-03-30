from sqlalchemy import (
    ARRAY,
    JSON,
    Boolean,
    Column,
    Float,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
    list,
)

from stripe_openapi.account import Account

from . import metadata

PaymentLink.Json = Table(
    "payment_link.json",
    metadata,
    Column(
        "active",
        Boolean,
        comment="Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated",
    ),
    Column(
        "after_completion",
        PaymentLinksResourceAfterCompletion,
        ForeignKey("PaymentLinksResourceAfterCompletion"),
    ),
    Column(
        "allow_promotion_codes",
        Boolean,
        comment="Whether user redeemable promotion codes are enabled",
    ),
    Column(
        "application_fee_amount",
        Integer,
        comment="The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account",
        nullable=True,
    ),
    Column(
        "application_fee_percent",
        Float,
        comment="This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account",
        nullable=True,
    ),
    Column(
        "automatic_tax",
        PaymentLinksResourceAutomaticTax,
        ForeignKey("PaymentLinksResourceAutomaticTax"),
    ),
    Column(
        "billing_address_collection",
        String,
        comment="Configuration for collecting the customer's billing address",
    ),
    Column(
        "consent_collection",
        PaymentLinksResourceConsentCollection,
        ForeignKey("PaymentLinksResourceConsentCollection"),
        comment="When set, provides configuration to gather active consent from customers",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "custom_fields",
        list,
        comment="Collect additional information from your customer using custom fields. Up to 2 fields are supported",
    ),
    Column(
        "custom_text",
        PaymentLinksResourceCustomText,
        ForeignKey("PaymentLinksResourceCustomText"),
    ),
    Column(
        "customer_creation",
        String,
        comment="Configuration for Customer creation during checkout",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column(
        "invoice_creation",
        PaymentLinksResourceInvoiceCreation,
        ForeignKey("PaymentLinksResourceInvoiceCreation"),
        comment="Configuration for creating invoice for payment mode payment links",
        nullable=True,
    ),
    Column(
        "line_items",
        JSON,
        comment="The line items representing what is being sold",
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
        comment="The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details",
        nullable=True,
    ),
    Column(
        "payment_intent_data",
        PaymentLinksResourcePaymentIntentData,
        ForeignKey("PaymentLinksResourcePaymentIntentData"),
        comment="Indicates the parameters to be passed to PaymentIntent creation during checkout",
        nullable=True,
    ),
    Column(
        "payment_method_collection",
        String,
        comment="Configuration for collecting a payment method during checkout",
    ),
    Column(
        "payment_method_types",
        ARRAY(String),
        comment="The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you've enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)",
        nullable=True,
    ),
    Column(
        "phone_number_collection",
        PaymentLinksResourcePhoneNumberCollection,
        ForeignKey("PaymentLinksResourcePhoneNumberCollection"),
    ),
    Column(
        "shipping_address_collection",
        PaymentLinksResourceShippingAddressCollection,
        ForeignKey("PaymentLinksResourceShippingAddressCollection"),
        comment="Configuration for collecting the customer's shipping address",
        nullable=True,
    ),
    Column(
        "shipping_options",
        list,
        comment="The shipping rate options applied to the session",
    ),
    Column(
        "submit_type",
        String,
        comment="Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button",
    ),
    Column(
        "subscription_data",
        PaymentLinksResourceSubscriptionData,
        ForeignKey("PaymentLinksResourceSubscriptionData"),
        comment="When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`",
        nullable=True,
    ),
    Column(
        "tax_id_collection",
        PaymentLinksResourceTaxIdCollection,
        ForeignKey("PaymentLinksResourceTaxIdCollection"),
    ),
    Column(
        "transfer_data",
        PaymentLinksResourceTransferData,
        ForeignKey("PaymentLinksResourceTransferData"),
        comment="The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to",
        nullable=True,
    ),
    Column("url", String, comment="The public URL that can be shared with customers"),
)
__all__ = ["payment_link.json"]
