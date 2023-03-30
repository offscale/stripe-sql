from sqlalchemy import (
    ARRAY,
    JSON,
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
)

from stripe_openapi.address import Address
from stripe_openapi.discount import Discount
from stripe_openapi.shipping import Shipping

from . import metadata

Customers.Json = Table(
    "customers.json",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="The customer's address",
        nullable=True,
    ),
    Column(
        "balance",
        Integer,
        comment="Current balance, if any, being stored on the customer. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that will be added to their next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account as invoices are finalized",
        nullable=True,
    ),
    Column(
        "cash_balance",
        CashBalance,
        ForeignKey("CashBalance"),
        comment='The current funds being held by Stripe on behalf of the customer. These funds can be applied towards payment intents with source "cash_balance". The settings[reconciliation_mode] field describes whether these funds are applied to such payment intents manually or automatically',
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes",
        nullable=True,
    ),
    Column(
        "default_source",
        PaymentSource,
        ForeignKey("PaymentSource"),
        comment="ID of the default payment source for the customer.\n\nIf you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) field instead",
        nullable=True,
    ),
    Column(
        "delinquent",
        Boolean,
        comment="When the customer's latest invoice is billed by charging automatically, `delinquent` is `true` if the invoice's latest charge failed. When the customer's latest invoice is billed by sending an invoice, `delinquent` is `true` if the invoice isn't paid by its due date.\n\nIf an invoice is marked uncollectible by [dunning](https://stripe.com/docs/billing/automatic-collection), `delinquent` doesn't get reset to `false`",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "discount",
        Discount,
        ForeignKey("Discount"),
        comment="Describes the current discount active on the customer, if there is one",
        nullable=True,
    ),
    Column("email", String, comment="The customer's email address", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column(
        "invoice_credit_balance",
        JSON,
        comment="The current multi-currency balances, if any, being stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that will be added to their next invoice denominated in that currency. These balances do not refer to any unpaid invoices. They solely track amounts that have yet to be successfully applied to any invoice. A balance in a particular currency is only applied to any invoice as an invoice in that currency is finalized",
        nullable=True,
    ),
    Column(
        "invoice_prefix",
        String,
        comment="The prefix for the customer used to generate unique invoice numbers",
        nullable=True,
    ),
    Column(
        "invoice_settings",
        InvoiceSettingCustomerSetting,
        ForeignKey("InvoiceSettingCustomerSetting"),
        nullable=True,
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "name",
        String,
        comment="The customer's full name or business name",
        nullable=True,
    ),
    Column(
        "next_invoice_sequence",
        Integer,
        comment="The suffix of the customer's next invoice number, e.g., 0001",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("phone", String, comment="The customer's phone number", nullable=True),
    Column(
        "preferred_locales",
        ARRAY(String),
        comment="The customer's preferred locales (languages), ordered by preference",
        nullable=True,
    ),
    Column(
        "shipping",
        Shipping,
        ForeignKey("Shipping"),
        comment="Mailing and shipping address for the customer. Appears on invoices emailed to this customer",
        nullable=True,
    ),
    Column(
        "sources", JSON, comment="The customer's payment sources, if any", nullable=True
    ),
    Column(
        "subscriptions",
        JSON,
        comment="The customer's current subscriptions, if any",
        nullable=True,
    ),
    Column("tax", CustomerTax, ForeignKey("CustomerTax"), nullable=True),
    Column(
        "tax_exempt",
        String,
        comment='Describes the customer\'s tax exemption status. One of `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the text **"Reverse charge"**',
        nullable=True,
    ),
    Column("tax_ids", JSON, comment="The customer's tax IDs", nullable=True),
    Column(
        "test_clock",
        Test_Helpers__TestClock,
        ForeignKey("Test_Helpers__TestClock"),
        comment="ID of the test clock this customer belongs to",
        nullable=True,
    ),
)
__all__ = ["customers.json"]
