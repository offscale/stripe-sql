from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsCardWalletJson = Table(
    "payment_method_details_card_walletjson",
    metadata,
    Column(
        "amex_express_checkout",
        PaymentMethodDetailsCardWalletAmexExpressCheckout,
        ForeignKey("PaymentMethodDetailsCardWalletAmexExpressCheckout"),
        nullable=True,
    ),
    Column(
        "apple_pay",
        PaymentMethodDetailsCardWalletApplePay,
        ForeignKey("PaymentMethodDetailsCardWalletApplePay"),
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
        PaymentMethodDetailsCardWalletGooglePay,
        ForeignKey("PaymentMethodDetailsCardWalletGooglePay"),
        nullable=True,
    ),
    Column(
        "masterpass",
        PaymentMethodDetailsCardWalletMasterpass,
        ForeignKey("PaymentMethodDetailsCardWalletMasterpass"),
        nullable=True,
    ),
    Column(
        "samsung_pay",
        PaymentMethodDetailsCardWalletSamsungPay,
        ForeignKey("PaymentMethodDetailsCardWalletSamsungPay"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, or `visa_checkout`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type",
    ),
    Column(
        "visa_checkout",
        PaymentMethodDetailsCardWalletVisaCheckout,
        ForeignKey("PaymentMethodDetailsCardWalletVisaCheckout"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_card_wallet.json"]
