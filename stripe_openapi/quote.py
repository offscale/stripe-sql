from sqlalchemy import Boolean, Column, Float, Integer, String

class Quote(Base):
    """
        A Quote is a way to model prices that you'd like to provide to a customer.
    
        Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    
        """
    __tablename__ = 'quote'
    amount_subtotal = Column(Integer, comment='Total before any discounts or taxes are applied')
    amount_total = Column(Integer, comment='Total after discounts and taxes are applied')
    application = Column(string | Application, comment='ID of the Connect Application that created the quote', nullable=True)
    application_fee_amount = Column(Integer, comment="The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote", nullable=True)
    application_fee_percent = Column(Float, comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote", nullable=True)
    automatic_tax = Column(QuotesResourceAutomaticTax)
    collection_method = Column(String, comment='Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`')
    computed = Column(QuotesResourceComputed)
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)', nullable=True)
    customer = Column(string | Customer, comment='The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed', nullable=True)
    default_tax_rates = Column(list, comment='The tax rates applied to this quote', nullable=True)
    description = Column(String, comment='A description that will be displayed on the quote PDF', nullable=True)
    discounts = Column(list, comment='The discounts applied to this quote')
    expires_at = Column(Integer, comment='The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch')
    footer = Column(String, comment='A footer that will be displayed on the quote PDF', nullable=True)
    from_quote = Column(QuotesResourceFromQuote, comment='Details of the quote that was cloned. See the [cloning documentation](https://stripe.com/docs/quotes/clone) for more details', nullable=True)
    header = Column(String, comment='A header that will be displayed on the quote PDF', nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    invoice = Column(string | Invoice, comment='The invoice that was created from this quote', nullable=True)
    invoice_settings = Column(InvoiceSettingQuoteSetting, comment='All invoices will be billed using the specified settings', nullable=True)
    line_items = Column(JSON, comment='A list of items the customer is being quoted for', nullable=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format')
    number = Column(String, comment='A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize)', nullable=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    on_behalf_of = Column(Account, comment='The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details', nullable=True)
    status = Column(String, comment='The status of the quote')
    status_transitions = Column(QuotesResourceStatusTransitions)
    subscription = Column(Subscription, comment='The subscription that was created or updated from this quote', nullable=True)
    subscription_data = Column(QuotesResourceSubscriptionDataSubscriptionData)
    subscription_schedule = Column(SubscriptionSchedule, comment='The subscription schedule that was created or updated from this quote', nullable=True)
    test_clock = Column(TestHelpers.TestClock, comment='ID of the test clock this quote belongs to', nullable=True)
    total_details = Column(QuotesResourceTotalDetails)
    transfer_data = Column(QuotesResourceTransferData, comment='The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Quote(amount_subtotal={amount_subtotal!r}, amount_total={amount_total!r}, application={application!r}, application_fee_amount={application_fee_amount!r}, application_fee_percent={application_fee_percent!r}, automatic_tax={automatic_tax!r}, collection_method={collection_method!r}, computed={computed!r}, created={created!r}, currency={currency!r}, customer={customer!r}, default_tax_rates={default_tax_rates!r}, description={description!r}, discounts={discounts!r}, expires_at={expires_at!r}, footer={footer!r}, from_quote={from_quote!r}, header={header!r}, id={id!r}, invoice={invoice!r}, invoice_settings={invoice_settings!r}, line_items={line_items!r}, livemode={livemode!r}, metadata={metadata!r}, number={number!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, status={status!r}, status_transitions={status_transitions!r}, subscription={subscription!r}, subscription_data={subscription_data!r}, subscription_schedule={subscription_schedule!r}, test_clock={test_clock!r}, total_details={total_details!r}, transfer_data={transfer_data!r})'.format(amount_subtotal=self.amount_subtotal, amount_total=self.amount_total, application=self.application, application_fee_amount=self.application_fee_amount, application_fee_percent=self.application_fee_percent, automatic_tax=self.automatic_tax, collection_method=self.collection_method, computed=self.computed, created=self.created, currency=self.currency, customer=self.customer, default_tax_rates=self.default_tax_rates, description=self.description, discounts=self.discounts, expires_at=self.expires_at, footer=self.footer, from_quote=self.from_quote, header=self.header, id=self.id, invoice=self.invoice, invoice_settings=self.invoice_settings, line_items=self.line_items, livemode=self.livemode, metadata=self.metadata, number=self.number, object=self.object, on_behalf_of=self.on_behalf_of, status=self.status, status_transitions=self.status_transitions, subscription=self.subscription, subscription_data=self.subscription_data, subscription_schedule=self.subscription_schedule, test_clock=self.test_clock, total_details=self.total_details, transfer_data=self.transfer_data)
__all__ = ['quote']