from sqlalchemy import JSON, Boolean, Column, Float, Integer, String

from . import Base


class TaxRate(Base):
    """
    Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

    Related guide: [Tax Rates](https://stripe.com/docs/billing/taxes/tax-rates).

    """

    __tablename__ = "tax_rate"
    active = Column(
        Boolean,
        comment="Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set",
    )
    country = Column(
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers",
        nullable=True,
    )
    display_name = Column(
        String,
        comment="The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    inclusive = Column(
        Boolean, comment="This specifies if the tax rate is inclusive or exclusive"
    )
    jurisdiction = Column(
        String,
        comment="The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice",
        nullable=True,
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
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    percentage = Column(
        Float, comment="This represents the tax rate percent out of 100"
    )
    state = Column(
        String,
        comment='[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States',
        nullable=True,
    )
    tax_type = Column(
        String,
        comment="The high-level tax type, such as `vat` or `sales_tax`",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TaxRate(active={active!r}, country={country!r}, created={created!r}, description={description!r}, display_name={display_name!r}, id={id!r}, inclusive={inclusive!r}, jurisdiction={jurisdiction!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, percentage={percentage!r}, state={state!r}, tax_type={tax_type!r})".format(
            active=self.active,
            country=self.country,
            created=self.created,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            inclusive=self.inclusive,
            jurisdiction=self.jurisdiction,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            percentage=self.percentage,
            state=self.state,
            tax_type=self.tax_type,
        )


__all__ = ["tax_rate"]
