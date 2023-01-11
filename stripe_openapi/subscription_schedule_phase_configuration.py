from sqlalchemy import JSON, Column, Float, ForeignKey, Identity, Integer, String, list

from . import Base


class SubscriptionSchedulePhaseConfiguration(Base):
    """
    A phase describes the plans, coupon, and trialing status of a subscription for a predefined time period.
    """

    __tablename__ = "subscription_schedule_phase_configuration"
    add_invoice_items = Column(
        list,
        comment="A list of prices and quantities that will generate invoice items appended to the next invoice for this phase",
    )
    application_fee_percent = Column(
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account during this phase of the schedule",
        nullable=True,
    )
    automatic_tax = Column(
        Integer, ForeignKey("schedules_phase_automatic_tax.id"), nullable=True
    )
    billing_cycle_anchor = Column(
        String,
        comment="Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)",
        nullable=True,
    )
    billing_thresholds = Column(
        Integer,
        ForeignKey("subscription_billing_thresholds.id"),
        comment="Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period",
        nullable=True,
    )
    collection_method = Column(
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`",
        nullable=True,
    )
    coupon = Column(
        Coupon,
        ForeignKey("DeletedCoupon"),
        comment="ID of the coupon to use during this phase of the subscription schedule",
        nullable=True,
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    default_payment_method = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings",
        nullable=True,
    )
    default_tax_rates = Column(
        list,
        comment="The default tax rates to apply to the subscription during this phase of the subscription schedule",
        nullable=True,
    )
    description = Column(
        String,
        comment="Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    )
    end_date = Column(
        Integer, comment="The end of this phase of the subscription schedule"
    )
    invoice_settings = Column(
        Integer,
        ForeignKey("invoice_setting_subscription_schedule_setting.id"),
        comment="The invoice settings applicable during this phase",
        nullable=True,
    )
    items = Column(
        list,
        comment="Subscription items to configure the subscription to during this phase of the subscription schedule",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered. Updating the underlying subscription's `metadata` directly will not affect the current phase's `metadata`",
        nullable=True,
    )
    on_behalf_of = Column(
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details",
        nullable=True,
    )
    proration_behavior = Column(
        String,
        comment="If the subscription schedule will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`",
    )
    start_date = Column(
        Integer, comment="The start of this phase of the subscription schedule"
    )
    transfer_data = Column(
        Integer,
        ForeignKey("subscription_transfer_data.id"),
        comment="The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices",
        nullable=True,
    )
    trial_end = Column(
        Integer, comment="When the trial ends within the phase", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionSchedulePhaseConfiguration(add_invoice_items={add_invoice_items!r}, application_fee_percent={application_fee_percent!r}, automatic_tax={automatic_tax!r}, billing_cycle_anchor={billing_cycle_anchor!r}, billing_thresholds={billing_thresholds!r}, collection_method={collection_method!r}, coupon={coupon!r}, currency={currency!r}, default_payment_method={default_payment_method!r}, default_tax_rates={default_tax_rates!r}, description={description!r}, end_date={end_date!r}, invoice_settings={invoice_settings!r}, items={items!r}, metadata={metadata!r}, on_behalf_of={on_behalf_of!r}, proration_behavior={proration_behavior!r}, start_date={start_date!r}, transfer_data={transfer_data!r}, trial_end={trial_end!r}, id={id!r})".format(
            add_invoice_items=self.add_invoice_items,
            application_fee_percent=self.application_fee_percent,
            automatic_tax=self.automatic_tax,
            billing_cycle_anchor=self.billing_cycle_anchor,
            billing_thresholds=self.billing_thresholds,
            collection_method=self.collection_method,
            coupon=self.coupon,
            currency=self.currency,
            default_payment_method=self.default_payment_method,
            default_tax_rates=self.default_tax_rates,
            description=self.description,
            end_date=self.end_date,
            invoice_settings=self.invoice_settings,
            items=self.items,
            metadata=self.metadata,
            on_behalf_of=self.on_behalf_of,
            proration_behavior=self.proration_behavior,
            start_date=self.start_date,
            transfer_data=self.transfer_data,
            trial_end=self.trial_end,
            id=self.id,
        )


__all__ = ["subscription_schedule_phase_configuration"]
