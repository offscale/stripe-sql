from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentIntentPaymentMethodOptionsJson = Table(
    "payment_intent_payment_method_optionsjson",
    metadata,
    Column(
        "acss_debit",
        PaymentIntentPaymentMethodOptionsAcssDebit,
        ForeignKey("PaymentIntentPaymentMethodOptionsAcssDebit"),
        nullable=True,
    ),
    Column(
        "affirm",
        PaymentMethodOptionsAffirm,
        ForeignKey("PaymentMethodOptionsAffirm"),
        nullable=True,
    ),
    Column(
        "afterpay_clearpay",
        PaymentMethodOptionsAfterpayClearpay,
        ForeignKey("PaymentMethodOptionsAfterpayClearpay"),
        nullable=True,
    ),
    Column(
        "alipay",
        PaymentMethodOptionsAlipay,
        ForeignKey("PaymentMethodOptionsAlipay"),
        nullable=True,
    ),
    Column(
        "au_becs_debit",
        PaymentIntentPaymentMethodOptionsAuBecsDebit,
        ForeignKey("PaymentIntentPaymentMethodOptionsAuBecsDebit"),
        nullable=True,
    ),
    Column(
        "bacs_debit",
        PaymentMethodOptionsBacsDebit,
        ForeignKey("PaymentMethodOptionsBacsDebit"),
        nullable=True,
    ),
    Column(
        "bancontact",
        PaymentMethodOptionsBancontact,
        ForeignKey("PaymentMethodOptionsBancontact"),
        nullable=True,
    ),
    Column(
        "blik",
        PaymentIntentPaymentMethodOptionsBlik,
        ForeignKey("PaymentIntentPaymentMethodOptionsBlik"),
        nullable=True,
    ),
    Column(
        "boleto",
        PaymentMethodOptionsBoleto,
        ForeignKey("PaymentMethodOptionsBoleto"),
        nullable=True,
    ),
    Column(
        "card",
        PaymentIntentPaymentMethodOptionsCard,
        ForeignKey("PaymentIntentPaymentMethodOptionsCard"),
        nullable=True,
    ),
    Column(
        "card_present",
        PaymentMethodOptionsCardPresent,
        ForeignKey("PaymentMethodOptionsCardPresent"),
        nullable=True,
    ),
    Column(
        "cashapp",
        PaymentMethodOptionsCashapp,
        ForeignKey("PaymentMethodOptionsCashapp"),
        nullable=True,
    ),
    Column(
        "customer_balance",
        PaymentMethodOptionsCustomerBalance,
        ForeignKey("PaymentMethodOptionsCustomerBalance"),
        nullable=True,
    ),
    Column(
        "eps",
        PaymentIntentPaymentMethodOptionsEps,
        ForeignKey("PaymentIntentPaymentMethodOptionsEps"),
        nullable=True,
    ),
    Column(
        "fpx",
        PaymentMethodOptionsFpx,
        ForeignKey("PaymentMethodOptionsFpx"),
        nullable=True,
    ),
    Column(
        "giropay",
        PaymentMethodOptionsGiropay,
        ForeignKey("PaymentMethodOptionsGiropay"),
        nullable=True,
    ),
    Column(
        "grabpay",
        PaymentMethodOptionsGrabpay,
        ForeignKey("PaymentMethodOptionsGrabpay"),
        nullable=True,
    ),
    Column(
        "ideal",
        PaymentMethodOptionsIdeal,
        ForeignKey("PaymentMethodOptionsIdeal"),
        nullable=True,
    ),
    Column(
        "interac_present",
        PaymentMethodOptionsInteracPresent,
        ForeignKey("PaymentMethodOptionsInteracPresent"),
        nullable=True,
    ),
    Column(
        "klarna",
        PaymentMethodOptionsKlarna,
        ForeignKey("PaymentMethodOptionsKlarna"),
        nullable=True,
    ),
    Column(
        "konbini",
        PaymentMethodOptionsKonbini,
        ForeignKey("PaymentMethodOptionsKonbini"),
        nullable=True,
    ),
    Column(
        "link",
        PaymentIntentPaymentMethodOptionsLink,
        ForeignKey("PaymentIntentPaymentMethodOptionsLink"),
        nullable=True,
    ),
    Column(
        "oxxo",
        PaymentMethodOptionsOxxo,
        ForeignKey("PaymentMethodOptionsOxxo"),
        nullable=True,
    ),
    Column(
        "p24",
        PaymentMethodOptionsP24,
        ForeignKey("PaymentMethodOptionsP24"),
        nullable=True,
    ),
    Column(
        "paynow",
        PaymentMethodOptionsPaynow,
        ForeignKey("PaymentMethodOptionsPaynow"),
        nullable=True,
    ),
    Column(
        "pix",
        PaymentMethodOptionsPix,
        ForeignKey("PaymentMethodOptionsPix"),
        nullable=True,
    ),
    Column(
        "promptpay",
        PaymentMethodOptionsPromptpay,
        ForeignKey("PaymentMethodOptionsPromptpay"),
        nullable=True,
    ),
    Column(
        "sepa_debit",
        PaymentIntentPaymentMethodOptionsSepaDebit,
        ForeignKey("PaymentIntentPaymentMethodOptionsSepaDebit"),
        nullable=True,
    ),
    Column(
        "sofort",
        PaymentMethodOptionsSofort,
        ForeignKey("PaymentMethodOptionsSofort"),
        nullable=True,
    ),
    Column(
        "us_bank_account",
        PaymentIntentPaymentMethodOptionsUsBankAccount,
        ForeignKey("PaymentIntentPaymentMethodOptionsUsBankAccount"),
        nullable=True,
    ),
    Column(
        "wechat_pay",
        PaymentMethodOptionsWechatPay,
        ForeignKey("PaymentMethodOptionsWechatPay"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_payment_method_options.json"]
