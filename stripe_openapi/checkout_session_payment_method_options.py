from sqlalchemy import Column, Integer


class Checkout_Session_Payment_Method_Options(Base):
    __tablename__ = "checkout_session_payment_method_options"
    acss_debit = Column(CheckoutAcssDebitPaymentMethodOptions, nullable=True)
    affirm = Column(CheckoutAffirmPaymentMethodOptions, nullable=True)
    afterpay_clearpay = Column(
        CheckoutAfterpayClearpayPaymentMethodOptions, nullable=True
    )
    alipay = Column(CheckoutAlipayPaymentMethodOptions, nullable=True)
    au_becs_debit = Column(CheckoutAuBecsDebitPaymentMethodOptions, nullable=True)
    bacs_debit = Column(CheckoutBacsDebitPaymentMethodOptions, nullable=True)
    bancontact = Column(CheckoutBancontactPaymentMethodOptions, nullable=True)
    boleto = Column(CheckoutBoletoPaymentMethodOptions, nullable=True)
    card = Column(CheckoutCardPaymentMethodOptions, nullable=True)
    customer_balance = Column(
        CheckoutCustomerBalancePaymentMethodOptions, nullable=True
    )
    eps = Column(CheckoutEpsPaymentMethodOptions, nullable=True)
    fpx = Column(CheckoutFpxPaymentMethodOptions, nullable=True)
    giropay = Column(CheckoutGiropayPaymentMethodOptions, nullable=True)
    grabpay = Column(CheckoutGrabPayPaymentMethodOptions, nullable=True)
    ideal = Column(CheckoutIdealPaymentMethodOptions, nullable=True)
    klarna = Column(CheckoutKlarnaPaymentMethodOptions, nullable=True)
    konbini = Column(CheckoutKonbiniPaymentMethodOptions, nullable=True)
    oxxo = Column(CheckoutOxxoPaymentMethodOptions, nullable=True)
    p24 = Column(CheckoutP24PaymentMethodOptions, nullable=True)
    paynow = Column(CheckoutPaynowPaymentMethodOptions, nullable=True)
    pix = Column(CheckoutPixPaymentMethodOptions, nullable=True)
    sepa_debit = Column(CheckoutSepaDebitPaymentMethodOptions, nullable=True)
    sofort = Column(CheckoutSofortPaymentMethodOptions, nullable=True)
    us_bank_account = Column(CheckoutUsBankAccountPaymentMethodOptions, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Checkout_Session_Payment_Method_Options(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, boleto={boleto!r}, card={card!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, klarna={klarna!r}, konbini={konbini!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            affirm=self.affirm,
            afterpay_clearpay=self.afterpay_clearpay,
            alipay=self.alipay,
            au_becs_debit=self.au_becs_debit,
            bacs_debit=self.bacs_debit,
            bancontact=self.bancontact,
            boleto=self.boleto,
            card=self.card,
            customer_balance=self.customer_balance,
            eps=self.eps,
            fpx=self.fpx,
            giropay=self.giropay,
            grabpay=self.grabpay,
            ideal=self.ideal,
            klarna=self.klarna,
            konbini=self.konbini,
            oxxo=self.oxxo,
            p24=self.p24,
            paynow=self.paynow,
            pix=self.pix,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["checkout_session_payment_method_options"]
