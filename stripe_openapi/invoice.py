from sqlalchemy import Boolean, Column, Integer, String


class Invoice(Base):
    """
    Invoices are statements of amounts owed by a customer, and are either

    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://stripe.com/docs/billing/invoices/workflow/#auto_advance), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://stripe.com/docs/billing/customer/balance).

    Related guide: [Send Invoices to Customers](https://stripe.com/docs/billing/invoices/sending).

    """

    __tablename__ = "invoice"
    account_country = Column(
        String,
        comment="The country of the business associated with this invoice, most often the business creating the invoice",
        nullable=True,
    )
    account_name = Column(
        String,
        comment="The public name of the business associated with this invoice, most often the business creating the invoice",
        nullable=True,
    )
    account_tax_ids = Column(
        list,
        comment="The account tax IDs associated with the invoice. Only editable when the invoice is a draft",
        nullable=True,
    )
    amount_due = Column(
        Integer,
        comment="Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`",
    )
    amount_paid = Column(Integer, comment="The amount, in %s, that was paid")
    amount_remaining = Column(
        Integer, comment="The difference between amount_due and amount_paid, in %s"
    )
    application = Column(
        string | Application,
        comment="ID of the Connect Application that created the invoice",
        nullable=True,
    )
    application_fee_amount = Column(
        Integer,
        comment="The fee in %s that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid",
        nullable=True,
    )
    attempt_count = Column(
        Integer,
        comment="Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule",
    )
    attempted = Column(
        Boolean,
        comment="Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users",
    )
    auto_advance = Column(
        Boolean,
        comment="Controls whether Stripe will perform [automatic collection](https://stripe.com/docs/billing/invoices/workflow/#auto_advance) of the invoice. When `false`, the invoice's state will not automatically advance without an explicit action",
        nullable=True,
    )
    automatic_tax = Column(AutomaticTax)
    billing_reason = Column(
        String,
        comment="Indicates the reason why the invoice was created. `subscription_cycle` indicates an invoice created by a subscription advancing into a new period. `subscription_create` indicates an invoice created due to creating a subscription. `subscription_update` indicates an invoice created due to updating a subscription. `subscription` is set for all old invoices to indicate either a change to a subscription or a period advancement. `manual` is set for all invoices unrelated to a subscription (for example: created via the invoice editor). The `upcoming` value is reserved for simulated invoices per the upcoming invoice endpoint. `subscription_threshold` indicates an invoice created due to a billing threshold being reached",
        nullable=True,
    )
    charge = Column(
        Charge,
        comment="ID of the latest charge generated for this invoice, if any",
        nullable=True,
    )
    collection_method = Column(
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    custom_fields = Column(
        list, comment="Custom fields displayed on the invoice", nullable=True
    )
    customer = Column(
        string | Customer,
        comment="The ID of the customer who will be billed",
        nullable=True,
    )
    customer_address = Column(
        Address,
        comment="The customer's address. Until the invoice is finalized, this field will equal `customer.address`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_email = Column(
        String,
        comment="The customer's email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_name = Column(
        String,
        comment="The customer's name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_phone = Column(
        String,
        comment="The customer's phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_shipping = Column(
        Shipping,
        comment="The customer's shipping information. Until the invoice is finalized, this field will equal `customer.shipping`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_tax_exempt = Column(
        String,
        comment="The customer's tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    customer_tax_ids = Column(
        list,
        comment="The customer's tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated",
        nullable=True,
    )
    default_payment_method = Column(
        PaymentMethod,
        comment="ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings",
        nullable=True,
    )
    default_source = Column(
        PaymentSource,
        comment="ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source",
        nullable=True,
    )
    default_tax_rates = Column(
        list, comment="The tax rates applied to this invoice, if any"
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard",
        nullable=True,
    )
    discount = Column(
        Discount,
        comment="Describes the current discount applied to this invoice, if there is one. Not populated if there are multiple discounts",
        nullable=True,
    )
    discounts = Column(
        list,
        comment="The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount",
        nullable=True,
    )
    due_date = Column(
        Integer,
        comment="The date on which payment for this invoice is due. This value will be `null` for invoices where `collection_method=charge_automatically`",
        nullable=True,
    )
    ending_balance = Column(
        Integer,
        comment="Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null",
        nullable=True,
    )
    footer = Column(String, comment="Footer displayed on the invoice", nullable=True)
    from_invoice = Column(
        InvoicesFromInvoice,
        comment="Details of the invoice that was cloned. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details",
        nullable=True,
    )
    hosted_invoice_url = Column(
        String,
        comment="The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null",
        nullable=True,
    )
    id = Column(
        String,
        comment="Unique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See [Retrieve an upcoming invoice](https://stripe.com/docs/api/invoices/upcoming) for more details",
        nullable=True,
        primary_key=True,
    )
    invoice_pdf = Column(
        String,
        comment="The link to download the PDF for the invoice. If the invoice has not been finalized yet, this will be null",
        nullable=True,
    )
    last_finalization_error = Column(
        ApiErrors,
        comment="The error encountered during the previous attempt to finalize the invoice. This field is cleared when the invoice is successfully finalized",
        nullable=True,
    )
    latest_revision = Column(
        Invoice,
        comment="The ID of the most recent non-draft revision of this invoice",
        nullable=True,
    )
    lines = Column(
        JSON,
        comment="The individual line items that make up the invoice. `lines` is sorted as follows: invoice items in reverse chronological order, followed by the subscription, if any",
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    next_payment_attempt = Column(
        Integer,
        comment="The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`",
        nullable=True,
    )
    number = Column(
        String,
        comment="A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    on_behalf_of = Column(
        Account,
        comment="The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details",
        nullable=True,
    )
    paid = Column(
        Boolean,
        comment="Whether payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance",
    )
    paid_out_of_band = Column(
        Boolean,
        comment="Returns true if the invoice was manually marked paid, returns false if the invoice hasn't been paid yet or was paid on Stripe",
    )
    payment_intent = Column(
        PaymentIntent,
        comment="The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent",
        nullable=True,
    )
    payment_settings = Column(InvoicesPaymentSettings)
    period_end = Column(
        Integer,
        comment="End of the usage period during which invoice items were added to this invoice",
    )
    period_start = Column(
        Integer,
        comment="Start of the usage period during which invoice items were added to this invoice",
    )
    post_payment_credit_notes_amount = Column(
        Integer,
        comment="Total amount of all post-payment credit notes issued for this invoice",
    )
    pre_payment_credit_notes_amount = Column(
        Integer,
        comment="Total amount of all pre-payment credit notes issued for this invoice",
    )
    quote = Column(
        Quote, comment="The quote this invoice was generated from", nullable=True
    )
    receipt_number = Column(
        String,
        comment="This is the transaction number that appears on email receipts sent for this invoice",
        nullable=True,
    )
    rendering_options = Column(
        InvoiceSettingRenderingOptions,
        comment="Options for invoice PDF rendering",
        nullable=True,
    )
    starting_balance = Column(
        Integer,
        comment="Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice",
    )
    statement_descriptor = Column(
        String,
        comment="Extra information about an invoice for the customer's credit card statement",
        nullable=True,
    )
    status = Column(
        String,
        comment="The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)",
        nullable=True,
    )
    status_transitions = Column(InvoicesStatusTransitions)
    subscription = Column(
        Subscription,
        comment="The subscription that this invoice was prepared for, if any",
        nullable=True,
    )
    subscription_proration_date = Column(
        Integer,
        comment="Only set for upcoming invoices that preview prorations. The time used to calculate prorations",
        nullable=True,
    )
    subtotal = Column(
        Integer,
        comment="Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated",
    )
    subtotal_excluding_tax = Column(
        Integer,
        comment="The integer amount in %s representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated",
        nullable=True,
    )
    tax = Column(
        Integer,
        comment="The amount of tax on this invoice. This is the sum of all the tax amounts on this invoice",
        nullable=True,
    )
    test_clock = Column(
        TestHelpers.TestClock,
        comment="ID of the test clock this invoice belongs to",
        nullable=True,
    )
    threshold_reason = Column(InvoiceThresholdReason, nullable=True)
    total = Column(Integer, comment="Total after discounts and taxes")
    total_discount_amounts = Column(
        list,
        comment="The aggregate amounts calculated per discount across all line items",
        nullable=True,
    )
    total_excluding_tax = Column(
        Integer,
        comment="The integer amount in %s representing the total amount of the invoice including all discounts but excluding all tax",
        nullable=True,
    )
    total_tax_amounts = Column(
        list, comment="The aggregate amounts calculated per tax rate for all line items"
    )
    transfer_data = Column(
        InvoiceTransferData,
        comment="The account (if any) the payment will be attributed to for tax reporting, and where funds from the payment will be transferred to for the invoice",
        nullable=True,
    )
    webhooks_delivered_at = Column(
        Integer,
        comment="Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://stripe.com/docs/billing/webhooks#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice(account_country={account_country!r}, account_name={account_name!r}, account_tax_ids={account_tax_ids!r}, amount_due={amount_due!r}, amount_paid={amount_paid!r}, amount_remaining={amount_remaining!r}, application={application!r}, application_fee_amount={application_fee_amount!r}, attempt_count={attempt_count!r}, attempted={attempted!r}, auto_advance={auto_advance!r}, automatic_tax={automatic_tax!r}, billing_reason={billing_reason!r}, charge={charge!r}, collection_method={collection_method!r}, created={created!r}, currency={currency!r}, custom_fields={custom_fields!r}, customer={customer!r}, customer_address={customer_address!r}, customer_email={customer_email!r}, customer_name={customer_name!r}, customer_phone={customer_phone!r}, customer_shipping={customer_shipping!r}, customer_tax_exempt={customer_tax_exempt!r}, customer_tax_ids={customer_tax_ids!r}, default_payment_method={default_payment_method!r}, default_source={default_source!r}, default_tax_rates={default_tax_rates!r}, description={description!r}, discount={discount!r}, discounts={discounts!r}, due_date={due_date!r}, ending_balance={ending_balance!r}, footer={footer!r}, from_invoice={from_invoice!r}, hosted_invoice_url={hosted_invoice_url!r}, id={id!r}, invoice_pdf={invoice_pdf!r}, last_finalization_error={last_finalization_error!r}, latest_revision={latest_revision!r}, lines={lines!r}, livemode={livemode!r}, metadata={metadata!r}, next_payment_attempt={next_payment_attempt!r}, number={number!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, paid={paid!r}, paid_out_of_band={paid_out_of_band!r}, payment_intent={payment_intent!r}, payment_settings={payment_settings!r}, period_end={period_end!r}, period_start={period_start!r}, post_payment_credit_notes_amount={post_payment_credit_notes_amount!r}, pre_payment_credit_notes_amount={pre_payment_credit_notes_amount!r}, quote={quote!r}, receipt_number={receipt_number!r}, rendering_options={rendering_options!r}, starting_balance={starting_balance!r}, statement_descriptor={statement_descriptor!r}, status={status!r}, status_transitions={status_transitions!r}, subscription={subscription!r}, subscription_proration_date={subscription_proration_date!r}, subtotal={subtotal!r}, subtotal_excluding_tax={subtotal_excluding_tax!r}, tax={tax!r}, test_clock={test_clock!r}, threshold_reason={threshold_reason!r}, total={total!r}, total_discount_amounts={total_discount_amounts!r}, total_excluding_tax={total_excluding_tax!r}, total_tax_amounts={total_tax_amounts!r}, transfer_data={transfer_data!r}, webhooks_delivered_at={webhooks_delivered_at!r})".format(
            account_country=self.account_country,
            account_name=self.account_name,
            account_tax_ids=self.account_tax_ids,
            amount_due=self.amount_due,
            amount_paid=self.amount_paid,
            amount_remaining=self.amount_remaining,
            application=self.application,
            application_fee_amount=self.application_fee_amount,
            attempt_count=self.attempt_count,
            attempted=self.attempted,
            auto_advance=self.auto_advance,
            automatic_tax=self.automatic_tax,
            billing_reason=self.billing_reason,
            charge=self.charge,
            collection_method=self.collection_method,
            created=self.created,
            currency=self.currency,
            custom_fields=self.custom_fields,
            customer=self.customer,
            customer_address=self.customer_address,
            customer_email=self.customer_email,
            customer_name=self.customer_name,
            customer_phone=self.customer_phone,
            customer_shipping=self.customer_shipping,
            customer_tax_exempt=self.customer_tax_exempt,
            customer_tax_ids=self.customer_tax_ids,
            default_payment_method=self.default_payment_method,
            default_source=self.default_source,
            default_tax_rates=self.default_tax_rates,
            description=self.description,
            discount=self.discount,
            discounts=self.discounts,
            due_date=self.due_date,
            ending_balance=self.ending_balance,
            footer=self.footer,
            from_invoice=self.from_invoice,
            hosted_invoice_url=self.hosted_invoice_url,
            id=self.id,
            invoice_pdf=self.invoice_pdf,
            last_finalization_error=self.last_finalization_error,
            latest_revision=self.latest_revision,
            lines=self.lines,
            livemode=self.livemode,
            metadata=self.metadata,
            next_payment_attempt=self.next_payment_attempt,
            number=self.number,
            object=self.object,
            on_behalf_of=self.on_behalf_of,
            paid=self.paid,
            paid_out_of_band=self.paid_out_of_band,
            payment_intent=self.payment_intent,
            payment_settings=self.payment_settings,
            period_end=self.period_end,
            period_start=self.period_start,
            post_payment_credit_notes_amount=self.post_payment_credit_notes_amount,
            pre_payment_credit_notes_amount=self.pre_payment_credit_notes_amount,
            quote=self.quote,
            receipt_number=self.receipt_number,
            rendering_options=self.rendering_options,
            starting_balance=self.starting_balance,
            statement_descriptor=self.statement_descriptor,
            status=self.status,
            status_transitions=self.status_transitions,
            subscription=self.subscription,
            subscription_proration_date=self.subscription_proration_date,
            subtotal=self.subtotal,
            subtotal_excluding_tax=self.subtotal_excluding_tax,
            tax=self.tax,
            test_clock=self.test_clock,
            threshold_reason=self.threshold_reason,
            total=self.total,
            total_discount_amounts=self.total_discount_amounts,
            total_excluding_tax=self.total_excluding_tax,
            total_tax_amounts=self.total_tax_amounts,
            transfer_data=self.transfer_data,
            webhooks_delivered_at=self.webhooks_delivered_at,
        )


__all__ = ["invoice"]
