from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.customer import Customer

from . import metadata

PaymentMethodJson = Table(
    "payment_methodjson",
    metadata,
    Column(
        "acss_debit",
        PaymentMethodAcssDebit,
        ForeignKey("PaymentMethodAcssDebit"),
        nullable=True,
    ),
    Column(
        "affirm", PaymentMethodAffirm, ForeignKey("PaymentMethodAffirm"), nullable=True
    ),
    Column(
        "afterpay_clearpay",
        PaymentMethodAfterpayClearpay,
        ForeignKey("PaymentMethodAfterpayClearpay"),
        nullable=True,
    ),
    Column(
        "alipay",
        PaymentFlowsPrivatePaymentMethodsAlipay,
        ForeignKey("PaymentFlowsPrivatePaymentMethodsAlipay"),
        nullable=True,
    ),
    Column(
        "au_becs_debit",
        PaymentMethodAuBecsDebit,
        ForeignKey("PaymentMethodAuBecsDebit"),
        nullable=True,
    ),
    Column(
        "bacs_debit",
        PaymentMethodBacsDebit,
        ForeignKey("PaymentMethodBacsDebit"),
        nullable=True,
    ),
    Column(
        "bancontact",
        PaymentMethodBancontact,
        ForeignKey("PaymentMethodBancontact"),
        nullable=True,
    ),
    Column("billing_details", BillingDetails, ForeignKey("BillingDetails")),
    Column("blik", PaymentMethodBlik, ForeignKey("PaymentMethodBlik"), nullable=True),
    Column(
        "boleto", PaymentMethodBoleto, ForeignKey("PaymentMethodBoleto"), nullable=True
    ),
    Column("card", PaymentMethodCard, ForeignKey("PaymentMethodCard"), nullable=True),
    Column(
        "card_present",
        PaymentMethodCardPresent,
        ForeignKey("PaymentMethodCardPresent"),
        nullable=True,
    ),
    Column(
        "cashapp",
        PaymentMethodCashapp,
        ForeignKey("PaymentMethodCashapp"),
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("Customer"),
        comment="The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer",
        nullable=True,
    ),
    Column(
        "customer_balance",
        PaymentMethodCustomerBalance,
        ForeignKey("PaymentMethodCustomerBalance"),
        nullable=True,
    ),
    Column("eps", PaymentMethodEps, ForeignKey("PaymentMethodEps"), nullable=True),
    Column("fpx", PaymentMethodFpx, ForeignKey("PaymentMethodFpx"), nullable=True),
    Column(
        "giropay",
        PaymentMethodGiropay,
        ForeignKey("PaymentMethodGiropay"),
        nullable=True,
    ),
    Column(
        "grabpay",
        PaymentMethodGrabpay,
        ForeignKey("PaymentMethodGrabpay"),
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "ideal", PaymentMethodIdeal, ForeignKey("PaymentMethodIdeal"), nullable=True
    ),
    Column(
        "interac_present",
        PaymentMethodInteracPresent,
        ForeignKey("PaymentMethodInteracPresent"),
        nullable=True,
    ),
    Column(
        "klarna", PaymentMethodKlarna, ForeignKey("PaymentMethodKlarna"), nullable=True
    ),
    Column(
        "konbini",
        PaymentMethodKonbini,
        ForeignKey("PaymentMethodKonbini"),
        nullable=True,
    ),
    Column("link", PaymentMethodLink, ForeignKey("PaymentMethodLink"), nullable=True),
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
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("oxxo", PaymentMethodOxxo, ForeignKey("PaymentMethodOxxo"), nullable=True),
    Column("p24", PaymentMethodP24, ForeignKey("PaymentMethodP24"), nullable=True),
    Column(
        "paynow", PaymentMethodPaynow, ForeignKey("PaymentMethodPaynow"), nullable=True
    ),
    Column("pix", PaymentMethodPix, ForeignKey("PaymentMethodPix"), nullable=True),
    Column(
        "promptpay",
        PaymentMethodPromptpay,
        ForeignKey("PaymentMethodPromptpay"),
        nullable=True,
    ),
    Column(
        "radar_options",
        RadarRadarOptions,
        ForeignKey("RadarRadarOptions"),
        nullable=True,
    ),
    Column(
        "sepa_debit",
        PaymentMethodSepaDebit,
        ForeignKey("PaymentMethodSepaDebit"),
        nullable=True,
    ),
    Column(
        "sofort", PaymentMethodSofort, ForeignKey("PaymentMethodSofort"), nullable=True
    ),
    Column(
        "type",
        String,
        comment="The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type",
    ),
    Column(
        "us_bank_account",
        PaymentMethodUsBankAccount,
        ForeignKey("PaymentMethodUsBankAccount"),
        nullable=True,
    ),
    Column(
        "wechat_pay",
        PaymentMethodWechatPay,
        ForeignKey("PaymentMethodWechatPay"),
        nullable=True,
    ),
)
__all__ = ["payment_method.json"]
