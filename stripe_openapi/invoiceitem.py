from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, list

from stripe_openapi.invoice_line_item_period import InvoiceLineItemPeriod
from stripe_openapi.test_helpers__test_clock import Test_Helpers__TestClock

from . import Base


class Invoiceitem(Base):
    """
    Sometimes you want to add a charge or credit to a customer, but actually

    charge or credit the customer's card only at the end of a regular billing
    cycle. This is useful for combining several charges (to minimize
    per-transaction fees), or for having Stripe tabulate your usage-based billing
    totals.

    Related guide: [Subscription Invoices](https://stripe.com/docs/billing/invoices/subscription#adding-upcoming-invoice-items).

    """

    __tablename__ = "invoiceitem"
    amount = Column(
        Integer,
        comment="Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The ID of the customer who will be billed when this invoice item is billed",
    )
    date = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    discountable = Column(
        Boolean,
        comment="If true, discounts will apply to this invoice item. Always false for prorations",
    )
    discounts = Column(
        list,
        comment="The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice = Column(
        Invoice,
        ForeignKey("Invoice"),
        comment="The ID of the invoice this invoice item belongs to",
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
    period = Column(InvoiceLineItemPeriod, ForeignKey("InvoiceLineItemPeriod"))
    plan = Column(
        Plan,
        ForeignKey("Plan"),
        comment="If the invoice item is a proration, the plan of the subscription that the proration was computed for",
        nullable=True,
    )
    price = Column(
        Price,
        ForeignKey("Price"),
        comment="The price of the invoice item",
        nullable=True,
    )
    proration = Column(
        Boolean,
        comment="Whether the invoice item was created automatically as a proration adjustment when the customer switched plans",
    )
    quantity = Column(
        Integer,
        comment="Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for",
    )
    subscription = Column(
        Subscription,
        ForeignKey("Subscription"),
        comment="The subscription that this invoice item has been created for, if any",
        nullable=True,
    )
    subscription_item = Column(
        String,
        comment="The subscription item that this invoice item has been created for, if any",
        nullable=True,
    )
    tax_rates = Column(
        list,
        comment="The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item",
        nullable=True,
    )
    test_clock = Column(
        Test_Helpers__TestClock,
        ForeignKey("Test_Helpers__TestClock"),
        comment="ID of the test clock this invoice item belongs to",
        nullable=True,
    )
    unit_amount = Column(
        Integer,
        comment="Unit amount (in the `currency` specified) of the invoice item",
        nullable=True,
    )
    unit_amount_decimal = Column(
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoiceitem(amount={amount!r}, currency={currency!r}, customer={customer!r}, date={date!r}, description={description!r}, discountable={discountable!r}, discounts={discounts!r}, id={id!r}, invoice={invoice!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, period={period!r}, plan={plan!r}, price={price!r}, proration={proration!r}, quantity={quantity!r}, subscription={subscription!r}, subscription_item={subscription_item!r}, tax_rates={tax_rates!r}, test_clock={test_clock!r}, unit_amount={unit_amount!r}, unit_amount_decimal={unit_amount_decimal!r})".format(
            amount=self.amount,
            currency=self.currency,
            customer=self.customer,
            date=self.date,
            description=self.description,
            discountable=self.discountable,
            discounts=self.discounts,
            id=self.id,
            invoice=self.invoice,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            period=self.period,
            plan=self.plan,
            price=self.price,
            proration=self.proration,
            quantity=self.quantity,
            subscription=self.subscription,
            subscription_item=self.subscription_item,
            tax_rates=self.tax_rates,
            test_clock=self.test_clock,
            unit_amount=self.unit_amount,
            unit_amount_decimal=self.unit_amount_decimal,
        )


__all__ = ["invoiceitem"]
