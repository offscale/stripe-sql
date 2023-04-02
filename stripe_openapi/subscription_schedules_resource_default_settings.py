from sqlalchemy import Column, Float, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.account import Account

from . import metadata

SubscriptionSchedulesResourceDefaultSettingsJson = Table(
    "subscription_schedules_resource_default_settingsjson",
    metadata,
    Column(
        "application_fee_percent",
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account during this phase of the schedule",
        nullable=True,
    ),
    Column(
        "automatic_tax",
        SubscriptionSchedulesResourceDefaultSettingsAutomaticTax,
        ForeignKey("SubscriptionSchedulesResourceDefaultSettingsAutomaticTax"),
        nullable=True,
    ),
    Column(
        "billing_cycle_anchor",
        String,
        comment="Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)",
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
        "default_payment_method",
        PaymentMethod,
        ForeignKey("PaymentMethod"),
        comment="ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    ),
    Column(
        "invoice_settings",
        InvoiceSettingSubscriptionScheduleSetting,
        ForeignKey("InvoiceSettingSubscriptionScheduleSetting"),
        comment="The subscription schedule's default invoice settings",
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
        "transfer_data",
        SubscriptionTransferData,
        ForeignKey("SubscriptionTransferData"),
        comment="The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedules_resource_default_settings.json"]
