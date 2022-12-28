from sqlalchemy import Boolean, Column, Float, Integer, String

class Payment_Link(Base):
    """
        A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.
    
        When a customer opens a payment link it will open a new [checkout session](https://stripe.com/docs/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://stripe.com/docs/api/events/types#event_types-checkout.session.completed) to track payments through payment links.
    
        Related guide: [Payment Links API](https://stripe.com/docs/payments/payment-links/api)
    
        """
    __tablename__ = 'payment_link'
    active = Column(Boolean, comment="Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated")
    after_completion = Column(PaymentLinksResourceAfterCompletion)
    allow_promotion_codes = Column(Boolean, comment='Whether user redeemable promotion codes are enabled')
    application_fee_amount = Column(Integer, comment="The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account", nullable=True)
    application_fee_percent = Column(Float, comment="This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account", nullable=True)
    automatic_tax = Column(PaymentLinksResourceAutomaticTax)
    billing_address_collection = Column(String, comment="Configuration for collecting the customer's billing address")
    consent_collection = Column(PaymentLinksResourceConsentCollection, comment='When set, provides configuration to gather active consent from customers', nullable=True)
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    custom_text = Column(PaymentLinksResourceCustomText)
    customer_creation = Column(String, comment='Configuration for Customer creation during checkout')
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    line_items = Column(JSON, comment='The line items representing what is being sold', nullable=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format')
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    on_behalf_of = Column(Account, comment='The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details', nullable=True)
    payment_intent_data = Column(PaymentLinksResourcePaymentIntentData, comment='Indicates the parameters to be passed to PaymentIntent creation during checkout', nullable=True)
    payment_method_collection = Column(String, comment='Configuration for collecting a payment method during checkout')
    payment_method_types = Column(ARRAY(String), comment="The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you've enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)", nullable=True)
    phone_number_collection = Column(PaymentLinksResourcePhoneNumberCollection)
    shipping_address_collection = Column(PaymentLinksResourceShippingAddressCollection, comment="Configuration for collecting the customer's shipping address", nullable=True)
    shipping_options = Column(list, comment='The shipping rate options applied to the session')
    submit_type = Column(String, comment='Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button')
    subscription_data = Column(PaymentLinksResourceSubscriptionData, comment='When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`', nullable=True)
    tax_id_collection = Column(PaymentLinksResourceTaxIdCollection)
    transfer_data = Column(PaymentLinksResourceTransferData, comment='The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to', nullable=True)
    url = Column(String, comment='The public URL that can be shared with customers')

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Link(active={active!r}, after_completion={after_completion!r}, allow_promotion_codes={allow_promotion_codes!r}, application_fee_amount={application_fee_amount!r}, application_fee_percent={application_fee_percent!r}, automatic_tax={automatic_tax!r}, billing_address_collection={billing_address_collection!r}, consent_collection={consent_collection!r}, currency={currency!r}, custom_text={custom_text!r}, customer_creation={customer_creation!r}, id={id!r}, line_items={line_items!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, payment_intent_data={payment_intent_data!r}, payment_method_collection={payment_method_collection!r}, payment_method_types={payment_method_types!r}, phone_number_collection={phone_number_collection!r}, shipping_address_collection={shipping_address_collection!r}, shipping_options={shipping_options!r}, submit_type={submit_type!r}, subscription_data={subscription_data!r}, tax_id_collection={tax_id_collection!r}, transfer_data={transfer_data!r}, url={url!r})'.format(active=self.active, after_completion=self.after_completion, allow_promotion_codes=self.allow_promotion_codes, application_fee_amount=self.application_fee_amount, application_fee_percent=self.application_fee_percent, automatic_tax=self.automatic_tax, billing_address_collection=self.billing_address_collection, consent_collection=self.consent_collection, currency=self.currency, custom_text=self.custom_text, customer_creation=self.customer_creation, id=self.id, line_items=self.line_items, livemode=self.livemode, metadata=self.metadata, object=self.object, on_behalf_of=self.on_behalf_of, payment_intent_data=self.payment_intent_data, payment_method_collection=self.payment_method_collection, payment_method_types=self.payment_method_types, phone_number_collection=self.phone_number_collection, shipping_address_collection=self.shipping_address_collection, shipping_options=self.shipping_options, submit_type=self.submit_type, subscription_data=self.subscription_data, tax_id_collection=self.tax_id_collection, transfer_data=self.transfer_data, url=self.url)
__all__ = ['payment_link']