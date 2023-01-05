from sqlalchemy import Column, Integer, String


class Payment_Method_Card_Wallet(Base):
    __tablename__ = "payment_method_card_wallet"
    amex_express_checkout = Column(
        PaymentMethodCardWalletAmexExpressCheckout, nullable=True
    )
    apple_pay = Column(PaymentMethodCardWalletApplePay, nullable=True)
    dynamic_last4 = Column(
        String,
        comment="(For tokenized numbers only.) The last four digits of the device account number",
        nullable=True,
    )
    google_pay = Column(PaymentMethodCardWalletGooglePay, nullable=True)
    masterpass = Column(PaymentMethodCardWalletMasterpass, nullable=True)
    samsung_pay = Column(PaymentMethodCardWalletSamsungPay, nullable=True)
    type = Column(
        String,
        comment="The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, or `visa_checkout`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type",
    )
    visa_checkout = Column(PaymentMethodCardWalletVisaCheckout, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Card_Wallet(amex_express_checkout={amex_express_checkout!r}, apple_pay={apple_pay!r}, dynamic_last4={dynamic_last4!r}, google_pay={google_pay!r}, masterpass={masterpass!r}, samsung_pay={samsung_pay!r}, type={type!r}, visa_checkout={visa_checkout!r}, id={id!r})".format(
            amex_express_checkout=self.amex_express_checkout,
            apple_pay=self.apple_pay,
            dynamic_last4=self.dynamic_last4,
            google_pay=self.google_pay,
            masterpass=self.masterpass,
            samsung_pay=self.samsung_pay,
            type=self.type,
            visa_checkout=self.visa_checkout,
            id=self.id,
        )


__all__ = ["payment_method_card_wallet"]
