from sqlalchemy import (
    JSON,
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
from stripe_openapi.coupon import Coupon

from . import metadata

SubscriptionSchedulePhaseConfiguration.Json = Table(
    "subscription_schedule_phase_configuration.json",
    metadata,
    Column(
        "add_invoice_items",
        list,
        comment="A list of prices and quantities that will generate invoice items appended to the next invoice for this phase",
    ),
    Column(
        "application_fee_percent",
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account during this phase of the schedule",
        nullable=True,
    ),
    Column(
        "automatic_tax",
        SchedulesPhaseAutomaticTax,
        ForeignKey("SchedulesPhaseAutomaticTax"),
        nullable=True,
    ),
    Column(
        "billing_cycle_anchor",
        String,
        comment="Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)",
        nullable=True,
    ),
    Column(
        "billing_thresholds",
        SubscriptionBillingThresholds,
        ForeignKey("SubscriptionBillingThresholds"),
        comment="Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period",
        nullable=True,
    ),
    Column(
        "collection_method",
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`",
        nullable=True,
    ),
    Column(
        "coupon",
        Coupon,
        ForeignKey("DeletedCoupon"),
        comment="ID of the coupon to use during this phase of the subscription schedule",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "default_payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings",
        nullable=True,
    ),
    Column(
        "default_tax_rates",
        list,
        comment="The default tax rates to apply to the subscription during this phase of the subscription schedule",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    ),
    Column(
        "end_date",
        Integer,
        comment="The end of this phase of the subscription schedule",
    ),
    Column(
        "invoice_settings",
        InvoiceSettingPhaseSetting,
        ForeignKey("InvoiceSettingPhaseSetting"),
        comment="The invoice settings applicable during this phase",
        nullable=True,
    ),
    Column(
        "items",
        list,
        comment="Subscription items to configure the subscription to during this phase of the subscription schedule",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered. Updating the underlying subscription's `metadata` directly will not affect the current phase's `metadata`",
        nullable=True,
    ),
    Column(
        "on_behalf_of",
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details",
        nullable=True,
    ),
    Column(
        "proration_behavior",
        String,
        comment="If the subscription schedule will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`",
    ),
    Column(
        "start_date",
        Integer,
        comment="The start of this phase of the subscription schedule",
    ),
    Column(
        "transfer_data",
        SubscriptionTransferData,
        ForeignKey("SubscriptionTransferData"),
        comment="The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices",
        nullable=True,
    ),
    Column(
        "trial_end",
        Integer,
        comment="When the trial ends within the phase",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedule_phase_configuration.json"]
