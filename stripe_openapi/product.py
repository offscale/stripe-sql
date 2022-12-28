from sqlalchemy import Boolean, Column, Integer, String

class Product(Base):
    """
        Products describe the specific goods or services you offer to your customers.
    
        For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
        They can be used in conjunction with [Prices](https://stripe.com/docs/api#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.
    
        Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription),
        [share a Payment Link](https://stripe.com/docs/payments/payment-links/overview),
        [accept payments with Checkout](https://stripe.com/docs/payments/accept-a-payment#create-product-prices-upfront),
        and more about [Products and Prices](https://stripe.com/docs/products-prices/overview)
    
        """
    __tablename__ = 'product'
    active = Column(Boolean, comment='Whether the product is currently available for purchase')
    attributes = Column(ARRAY(String), comment='A list of up to 5 attributes that each SKU can provide values for (e.g., `["color", "size"]`)', nullable=True)
    caption = Column(String, comment='A short one-line description of the product, meant to be displayable to the customer. Only applicable to products of `type=good`', nullable=True)
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    deactivate_on = Column(ARRAY(String), comment='An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`', nullable=True)
    default_price = Column(Price, comment='The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product', nullable=True)
    description = Column(String, comment="The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes", nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    images = Column(ARRAY(String), comment='A list of up to 8 URLs of images for this product, meant to be displayable to the customer')
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    metadata = Column(JSON, comment='Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format')
    name = Column(String, comment="The product's name, meant to be displayable to the customer")
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    package_dimensions = Column(PackageDimensions, comment='The dimensions of this product for shipping purposes', nullable=True)
    shippable = Column(Boolean, comment='Whether this product is shipped (i.e., physical goods)', nullable=True)
    statement_descriptor = Column(String, comment="Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used", nullable=True)
    tax_code = Column(TaxCode, comment='A [tax code](https://stripe.com/docs/tax/tax-categories) ID', nullable=True)
    type = Column(String, comment='The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans')
    unit_label = Column(String, comment='A label that represents units of this product in Stripe and on customers’ receipts and invoices. When set, this will be included in associated invoice line item descriptions', nullable=True)
    updated = Column(Integer, comment='Time at which the object was last updated. Measured in seconds since the Unix epoch')
    url = Column(String, comment='A URL of a publicly-accessible webpage for this product', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Product(active={active!r}, attributes={attributes!r}, caption={caption!r}, created={created!r}, deactivate_on={deactivate_on!r}, default_price={default_price!r}, description={description!r}, id={id!r}, images={images!r}, livemode={livemode!r}, metadata={metadata!r}, name={name!r}, object={object!r}, package_dimensions={package_dimensions!r}, shippable={shippable!r}, statement_descriptor={statement_descriptor!r}, tax_code={tax_code!r}, type={type!r}, unit_label={unit_label!r}, updated={updated!r}, url={url!r})'.format(active=self.active, attributes=self.attributes, caption=self.caption, created=self.created, deactivate_on=self.deactivate_on, default_price=self.default_price, description=self.description, id=self.id, images=self.images, livemode=self.livemode, metadata=self.metadata, name=self.name, object=self.object, package_dimensions=self.package_dimensions, shippable=self.shippable, statement_descriptor=self.statement_descriptor, tax_code=self.tax_code, type=self.type, unit_label=self.unit_label, updated=self.updated, url=self.url)
__all__ = ['product']