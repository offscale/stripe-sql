from sqlalchemy import Boolean, Column, Integer, String

class Line_Item(Base):
    __tablename__ = 'line_item'
    amount = Column(Integer, comment='The amount, in %s')
    amount_excluding_tax = Column(Integer, comment='The integer amount in %s representing the amount for this line item, excluding all tax and discounts', nullable=True)
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    description = Column(String, comment='An arbitrary string attached to the object. Often useful for displaying to users', nullable=True)
    discount_amounts = Column(list, comment='The amount of discount calculated per discount for this line item', nullable=True)
    discountable = Column(Boolean, comment='If true, discounts will apply to this line item. Always false for prorations')
    discounts = Column(list, comment='The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount', nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    invoice_item = Column(String, comment='The ID of the [invoice item](https://stripe.com/docs/api/invoiceitems) associated with this line item if any', nullable=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription` this will reflect the metadata of the subscription that caused the line item to be created')
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    period = Column(InvoiceLineItemPeriod)
    plan = Column(Plan, comment='The plan of the subscription, if the line item is a subscription or a proration', nullable=True)
    price = Column(Price, comment='The price of the line item', nullable=True)
    proration = Column(Boolean, comment='Whether this is a proration')
    proration_details = Column(InvoicesLineItemsProrationDetails, comment='Additional details for proration line items', nullable=True)
    quantity = Column(Integer, comment='The quantity of the subscription, if the line item is a subscription or a proration', nullable=True)
    subscription = Column(String, comment='The subscription that the invoice item pertains to, if any', nullable=True)
    subscription_item = Column(String, comment='The subscription item that generated this invoice item. Left empty if the line item is not an explicit result of a subscription', nullable=True)
    tax_amounts = Column(list, comment='The amount of tax calculated per tax rate for this line item', nullable=True)
    tax_rates = Column(list, comment='The tax rates which apply to the line item', nullable=True)
    type = Column(String, comment='A string identifying the type of the source of this line item, either an `invoiceitem` or a `subscription`')
    unit_amount_excluding_tax = Column(String, comment='The amount in %s representing the unit amount for this line item, excluding all tax and discounts', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Line_Item(amount={amount!r}, amount_excluding_tax={amount_excluding_tax!r}, currency={currency!r}, description={description!r}, discount_amounts={discount_amounts!r}, discountable={discountable!r}, discounts={discounts!r}, id={id!r}, invoice_item={invoice_item!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, period={period!r}, plan={plan!r}, price={price!r}, proration={proration!r}, proration_details={proration_details!r}, quantity={quantity!r}, subscription={subscription!r}, subscription_item={subscription_item!r}, tax_amounts={tax_amounts!r}, tax_rates={tax_rates!r}, type={type!r}, unit_amount_excluding_tax={unit_amount_excluding_tax!r})'.format(amount=self.amount, amount_excluding_tax=self.amount_excluding_tax, currency=self.currency, description=self.description, discount_amounts=self.discount_amounts, discountable=self.discountable, discounts=self.discounts, id=self.id, invoice_item=self.invoice_item, livemode=self.livemode, metadata=self.metadata, object=self.object, period=self.period, plan=self.plan, price=self.price, proration=self.proration, proration_details=self.proration_details, quantity=self.quantity, subscription=self.subscription, subscription_item=self.subscription_item, tax_amounts=self.tax_amounts, tax_rates=self.tax_rates, type=self.type, unit_amount_excluding_tax=self.unit_amount_excluding_tax)
__all__ = ['line_item']