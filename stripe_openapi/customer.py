from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String

from stripe_openapi.cash_balance import CashBalance
from stripe_openapi.payment_source import PaymentSource
from stripe_openapi.test_helpers import TestHelpers

from . import Base


class Customer(Base):
    """
    This object represents a customer of your business. It lets you create recurring charges and track payments that belong to the same customer.

    Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment).

    """

    __tablename__ = "customer"
    address = Column(
        Address, comment="[[FK(Address)]] The customer's address", nullable=True
    )
    balance = Column(
        Integer,
        comment="Current balance, if any, being stored on the customer. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that will be added to their next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account as invoices are finalized",
        nullable=True,
    )
    cash_balance = Column(
        CashBalance,
        comment='[[FK(CashBalance)]] The current funds being held by Stripe on behalf of the customer. These funds can be applied towards payment intents with source "cash_balance". The settings[reconciliation_mode] field describes whether these funds are applied to such payment intents manually or automatically',
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes",
        nullable=True,
    )
    default_source = Column(
        PaymentSource,
        comment="[[FK(PaymentSource)]] ID of the default payment source for the customer.\n\nIf you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) field instead",
        nullable=True,
    )
    delinquent = Column(
        Boolean,
        comment="When the customer's latest invoice is billed by charging automatically, `delinquent` is `true` if the invoice's latest charge failed. When the customer's latest invoice is billed by sending an invoice, `delinquent` is `true` if the invoice isn't paid by its due date.\n\nIf an invoice is marked uncollectible by [dunning](https://stripe.com/docs/billing/automatic-collection), `delinquent` doesn't get reset to `false`",
        nullable=True,
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    discount = Column(
        Discount,
        comment="[[FK(Discount)]] Describes the current discount active on the customer, if there is one",
        nullable=True,
    )
    email = Column(String, comment="The customer's email address", nullable=True)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice_credit_balance = Column(
        JSON,
        comment="The current multi-currency balances, if any, being stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that will be added to their next invoice denominated in that currency. These balances do not refer to any unpaid invoices. They solely track amounts that have yet to be successfully applied to any invoice. A balance in a particular currency is only applied to any invoice as an invoice in that currency is finalized",
        nullable=True,
    )
    invoice_prefix = Column(
        String,
        comment="The prefix for the customer used to generate unique invoice numbers",
        nullable=True,
    )
    invoice_settings = Column(
        Integer, ForeignKey("invoice_setting_customer_setting.id"), nullable=True
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
    name = Column(
        String, comment="The customer's full name or business name", nullable=True
    )
    next_invoice_sequence = Column(
        Integer,
        comment="The suffix of the customer's next invoice number, e.g., 0001",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    phone = Column(String, comment="The customer's phone number", nullable=True)
    preferred_locales = Column(
        ARRAY(String),
        comment="The customer's preferred locales (languages), ordered by preference",
        nullable=True,
    )
    shipping = Column(
        Shipping,
        comment="[[FK(Shipping)]] Mailing and shipping address for the customer. Appears on invoices emailed to this customer",
        nullable=True,
    )
    sources = Column(
        JSON, comment="The customer's payment sources, if any", nullable=True
    )
    subscriptions = Column(
        JSON, comment="The customer's current subscriptions, if any", nullable=True
    )
    tax = Column(Integer, ForeignKey("customer_tax.id"), nullable=True)
    tax_exempt = Column(
        String,
        comment='Describes the customer\'s tax exemption status. One of `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the text **"Reverse charge"**',
        nullable=True,
    )
    tax_ids = Column(JSON, comment="The customer's tax IDs", nullable=True)
    test_clock = Column(
        TestHelpers.TestClock,
        comment="[[FK(TestHelpers.TestClock)]] ID of the test clock this customer belongs to",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer(address={address!r}, balance={balance!r}, cash_balance={cash_balance!r}, created={created!r}, currency={currency!r}, default_source={default_source!r}, delinquent={delinquent!r}, description={description!r}, discount={discount!r}, email={email!r}, id={id!r}, invoice_credit_balance={invoice_credit_balance!r}, invoice_prefix={invoice_prefix!r}, invoice_settings={invoice_settings!r}, livemode={livemode!r}, metadata={metadata!r}, name={name!r}, next_invoice_sequence={next_invoice_sequence!r}, object={object!r}, phone={phone!r}, preferred_locales={preferred_locales!r}, shipping={shipping!r}, sources={sources!r}, subscriptions={subscriptions!r}, tax={tax!r}, tax_exempt={tax_exempt!r}, tax_ids={tax_ids!r}, test_clock={test_clock!r})".format(
            address=self.address,
            balance=self.balance,
            cash_balance=self.cash_balance,
            created=self.created,
            currency=self.currency,
            default_source=self.default_source,
            delinquent=self.delinquent,
            description=self.description,
            discount=self.discount,
            email=self.email,
            id=self.id,
            invoice_credit_balance=self.invoice_credit_balance,
            invoice_prefix=self.invoice_prefix,
            invoice_settings=self.invoice_settings,
            livemode=self.livemode,
            metadata=self.metadata,
            name=self.name,
            next_invoice_sequence=self.next_invoice_sequence,
            object=self.object,
            phone=self.phone,
            preferred_locales=self.preferred_locales,
            shipping=self.shipping,
            sources=self.sources,
            subscriptions=self.subscriptions,
            tax=self.tax,
            tax_exempt=self.tax_exempt,
            tax_ids=self.tax_ids,
            test_clock=self.test_clock,
        )


__all__ = ["customer"]
