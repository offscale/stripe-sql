from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
    list,
)

from stripe_openapi.account import Account
from stripe_openapi.application import Application
from stripe_openapi.customer import Customer
from stripe_openapi.invoice import Invoice
from stripe_openapi.subscription import Subscription

from . import metadata

QuoteJson = Table(
    "quotejson",
    metadata,
    Column(
        "amount_subtotal",
        Integer,
        comment="Total before any discounts or taxes are applied",
    ),
    Column(
        "amount_total", Integer, comment="Total after discounts and taxes are applied"
    ),
    Column(
        "application",
        Application,
        ForeignKey("DeletedApplication"),
        comment="ID of the Connect Application that created the quote",
        nullable=True,
    ),
    Column(
        "application_fee_amount",
        Integer,
        comment="The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote",
        nullable=True,
    ),
    Column(
        "application_fee_percent",
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote",
        nullable=True,
    ),
    Column(
        "automatic_tax",
        QuotesResourceAutomaticTax,
        ForeignKey("QuotesResourceAutomaticTax"),
    ),
    Column(
        "collection_method",
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`",
    ),
    Column("computed", QuotesResourceComputed, ForeignKey("QuotesResourceComputed")),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed",
        nullable=True,
    ),
    Column(
        "default_tax_rates",
        list,
        comment="The tax rates applied to this quote",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="A description that will be displayed on the quote PDF",
        nullable=True,
    ),
    Column("discounts", list, comment="The discounts applied to this quote"),
    Column(
        "expires_at",
        Integer,
        comment="The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch",
    ),
    Column(
        "footer",
        String,
        comment="A footer that will be displayed on the quote PDF",
        nullable=True,
    ),
    Column(
        "from_quote",
        QuotesResourceFromQuote,
        ForeignKey("QuotesResourceFromQuote"),
        comment="Details of the quote that was cloned. See the [cloning documentation](https://stripe.com/docs/quotes/clone) for more details",
        nullable=True,
    ),
    Column(
        "header",
        String,
        comment="A header that will be displayed on the quote PDF",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        Invoice,
        ForeignKey("DeletedInvoice"),
        comment="The invoice that was created from this quote",
        nullable=True,
    ),
    Column(
        "invoice_settings",
        InvoiceSettingQuoteSetting,
        ForeignKey("InvoiceSettingQuoteSetting"),
        comment="All invoices will be billed using the specified settings",
        nullable=True,
    ),
    Column(
        "line_items",
        JSON,
        comment="A list of items the customer is being quoted for",
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
        "number",
        String,
        comment="A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize)",
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
        comment="The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details",
        nullable=True,
    ),
    Column("status", String, comment="The status of the quote"),
    Column(
        "status_transitions",
        QuotesResourceStatusTransitions,
        ForeignKey("QuotesResourceStatusTransitions"),
    ),
    Column(
        "subscription",
        Subscription,
        ForeignKey("Subscription"),
        comment="The subscription that was created or updated from this quote",
        nullable=True,
    ),
    Column(
        "subscription_data",
        QuotesResourceSubscriptionDataSubscriptionData,
        ForeignKey("QuotesResourceSubscriptionDataSubscriptionData"),
    ),
    Column(
        "subscription_schedule",
        SubscriptionSchedule,
        ForeignKey("SubscriptionSchedule"),
        comment="The subscription schedule that was created or updated from this quote",
        nullable=True,
    ),
    Column(
        "test_clock",
        Test_Helpers__TestClock,
        ForeignKey("Test_Helpers__TestClock"),
        comment="ID of the test clock this quote belongs to",
        nullable=True,
    ),
    Column(
        "total_details",
        QuotesResourceTotalDetails,
        ForeignKey("QuotesResourceTotalDetails"),
    ),
    Column(
        "transfer_data",
        QuotesResourceTransferData,
        ForeignKey("QuotesResourceTransferData"),
        comment="The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices",
        nullable=True,
    ),
)
__all__ = ["quote.json"]
