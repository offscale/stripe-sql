from sqlalchemy import Boolean, Column, Float, Integer, String


class Subscription(Base):
    """
    Subscriptions allow you to charge a customer on a recurring basis.

    Related guide: [Creating Subscriptions](https://stripe.com/docs/billing/subscriptions/creating).

    """

    __tablename__ = "subscription"
    application = Column(
        string | Application,
        comment="ID of the Connect Application that created the subscription",
        nullable=True,
    )
    application_fee_percent = Column(
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account",
        nullable=True,
    )
    automatic_tax = Column(SubscriptionAutomaticTax)
    billing_cycle_anchor = Column(
        Integer,
        comment="Determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format",
    )
    billing_thresholds = Column(
        SubscriptionBillingThresholds,
        comment="Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period",
        nullable=True,
    )
    cancel_at = Column(
        Integer,
        comment="A date in the future at which the subscription will automatically get canceled",
        nullable=True,
    )
    cancel_at_period_end = Column(
        Boolean,
        comment="If the subscription has been canceled with the `at_period_end` flag set to `true`, `cancel_at_period_end` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period",
    )
    canceled_at = Column(
        Integer,
        comment="If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state",
        nullable=True,
    )
    collection_method = Column(
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    current_period_end = Column(
        Integer,
        comment="End of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created",
    )
    current_period_start = Column(
        Integer,
        comment="Start of the current period that the subscription has been invoiced for",
    )
    customer = Column(
        string | Customer, comment="ID of the customer who owns the subscription"
    )
    days_until_due = Column(
        Integer,
        comment="Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`",
        nullable=True,
    )
    default_payment_method = Column(
        PaymentMethod,
        comment="ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)",
        nullable=True,
    )
    default_source = Column(
        PaymentSource,
        comment="ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)",
        nullable=True,
    )
    default_tax_rates = Column(
        list,
        comment="The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription",
        nullable=True,
    )
    description = Column(
        String,
        comment="The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces",
        nullable=True,
    )
    discount = Column(
        Discount,
        comment="Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis",
        nullable=True,
    )
    ended_at = Column(
        Integer,
        comment="If the subscription has ended, the date the subscription ended",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    items = Column(
        JSON, comment="List of subscription items, each with an attached price"
    )
    latest_invoice = Column(
        Invoice,
        comment="The most recent invoice this subscription has generated",
        nullable=True,
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    next_pending_invoice_item_invoice = Column(
        Integer,
        comment="Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    on_behalf_of = Column(
        Account,
        comment="The account (if any) the charge was made on behalf of for charges associated with this subscription. See the Connect documentation for details",
        nullable=True,
    )
    pause_collection = Column(
        SubscriptionsResourcePauseCollection,
        comment="If specified, payment collection for this subscription will be paused",
        nullable=True,
    )
    payment_settings = Column(
        SubscriptionsResourcePaymentSettings,
        comment="Payment settings passed on to invoices created by the subscription",
        nullable=True,
    )
    pending_invoice_item_interval = Column(
        SubscriptionPendingInvoiceItemInterval,
        comment="Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval",
        nullable=True,
    )
    pending_setup_intent = Column(
        SetupIntent,
        comment="You can use this [SetupIntent](https://stripe.com/docs/api/setup_intents) to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication#scenario-2)",
        nullable=True,
    )
    pending_update = Column(
        SubscriptionsResourcePendingUpdate,
        comment="If specified, [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates) that will be applied to the subscription once the `latest_invoice` has been paid",
        nullable=True,
    )
    schedule = Column(
        SubscriptionSchedule,
        comment="The schedule attached to the subscription",
        nullable=True,
    )
    start_date = Column(
        Integer,
        comment="Date when the subscription was first created. The date might differ from the `created` date due to backdating",
    )
    status = Column(
        String,
        comment="Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, or `unpaid`. \n\nFor `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this state can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` state. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal state, the open invoice will be voided and no further invoices will be generated. \n\nA subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over. \n\nIf subscription `collection_method=charge_automatically` it becomes `past_due` when payment to renew it fails and `canceled` or `unpaid` (depending on your subscriptions settings) when Stripe has exhausted all payment retry attempts. \n\nIf subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices",
    )
    test_clock = Column(
        TestHelpers.TestClock,
        comment="ID of the test clock this subscription belongs to",
        nullable=True,
    )
    transfer_data = Column(
        SubscriptionTransferData,
        comment="The account (if any) the subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices",
        nullable=True,
    )
    trial_end = Column(
        Integer,
        comment="If the subscription has a trial, the end of that trial",
        nullable=True,
    )
    trial_start = Column(
        Integer,
        comment="If the subscription has a trial, the beginning of that trial",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription(application={application!r}, application_fee_percent={application_fee_percent!r}, automatic_tax={automatic_tax!r}, billing_cycle_anchor={billing_cycle_anchor!r}, billing_thresholds={billing_thresholds!r}, cancel_at={cancel_at!r}, cancel_at_period_end={cancel_at_period_end!r}, canceled_at={canceled_at!r}, collection_method={collection_method!r}, created={created!r}, currency={currency!r}, current_period_end={current_period_end!r}, current_period_start={current_period_start!r}, customer={customer!r}, days_until_due={days_until_due!r}, default_payment_method={default_payment_method!r}, default_source={default_source!r}, default_tax_rates={default_tax_rates!r}, description={description!r}, discount={discount!r}, ended_at={ended_at!r}, id={id!r}, items={items!r}, latest_invoice={latest_invoice!r}, livemode={livemode!r}, metadata={metadata!r}, next_pending_invoice_item_invoice={next_pending_invoice_item_invoice!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, pause_collection={pause_collection!r}, payment_settings={payment_settings!r}, pending_invoice_item_interval={pending_invoice_item_interval!r}, pending_setup_intent={pending_setup_intent!r}, pending_update={pending_update!r}, schedule={schedule!r}, start_date={start_date!r}, status={status!r}, test_clock={test_clock!r}, transfer_data={transfer_data!r}, trial_end={trial_end!r}, trial_start={trial_start!r})".format(
            application=self.application,
            application_fee_percent=self.application_fee_percent,
            automatic_tax=self.automatic_tax,
            billing_cycle_anchor=self.billing_cycle_anchor,
            billing_thresholds=self.billing_thresholds,
            cancel_at=self.cancel_at,
            cancel_at_period_end=self.cancel_at_period_end,
            canceled_at=self.canceled_at,
            collection_method=self.collection_method,
            created=self.created,
            currency=self.currency,
            current_period_end=self.current_period_end,
            current_period_start=self.current_period_start,
            customer=self.customer,
            days_until_due=self.days_until_due,
            default_payment_method=self.default_payment_method,
            default_source=self.default_source,
            default_tax_rates=self.default_tax_rates,
            description=self.description,
            discount=self.discount,
            ended_at=self.ended_at,
            id=self.id,
            items=self.items,
            latest_invoice=self.latest_invoice,
            livemode=self.livemode,
            metadata=self.metadata,
            next_pending_invoice_item_invoice=self.next_pending_invoice_item_invoice,
            object=self.object,
            on_behalf_of=self.on_behalf_of,
            pause_collection=self.pause_collection,
            payment_settings=self.payment_settings,
            pending_invoice_item_interval=self.pending_invoice_item_interval,
            pending_setup_intent=self.pending_setup_intent,
            pending_update=self.pending_update,
            schedule=self.schedule,
            start_date=self.start_date,
            status=self.status,
            test_clock=self.test_clock,
            transfer_data=self.transfer_data,
            trial_end=self.trial_end,
            trial_start=self.trial_start,
        )


__all__ = ["subscription"]
