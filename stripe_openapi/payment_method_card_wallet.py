from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentMethodCardWalletJson = Table(
    "payment_method_card_walletjson",
    metadata,
    Column(
        "amex_express_checkout",
        PaymentMethodCardWalletAmexExpressCheckout,
        ForeignKey("PaymentMethodCardWalletAmexExpressCheckout"),
        nullable=True,
    ),
    Column(
        "apple_pay",
        PaymentMethodCardWalletApplePay,
        ForeignKey("PaymentMethodCardWalletApplePay"),
        nullable=True,
    ),
    Column(
        "dynamic_last4",
        String,
        comment="(For tokenized numbers only.) The last four digits of the device account number",
        nullable=True,
    ),
    Column(
        "google_pay",
        PaymentMethodCardWalletGooglePay,
        ForeignKey("PaymentMethodCardWalletGooglePay"),
        nullable=True,
    ),
    Column(
        "masterpass",
        PaymentMethodCardWalletMasterpass,
        ForeignKey("PaymentMethodCardWalletMasterpass"),
        nullable=True,
    ),
    Column(
        "samsung_pay",
        PaymentMethodCardWalletSamsungPay,
        ForeignKey("PaymentMethodCardWalletSamsungPay"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, or `visa_checkout`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type",
    ),
    Column(
        "visa_checkout",
        PaymentMethodCardWalletVisaCheckout,
        ForeignKey("PaymentMethodCardWalletVisaCheckout"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_wallet.json"]
