from sqlalchemy import Column, Integer

class Payment_Intent_Payment_Method_Options(Base):
    __tablename__ = 'payment_intent_payment_method_options'
    acss_debit = Column(PaymentIntentPaymentMethodOptionsAcssDebit, nullable=True)
    affirm = Column(PaymentMethodOptionsAffirm, nullable=True)
    afterpay_clearpay = Column(PaymentMethodOptionsAfterpayClearpay, nullable=True)
    alipay = Column(PaymentMethodOptionsAlipay, nullable=True)
    au_becs_debit = Column(PaymentIntentPaymentMethodOptionsAuBecsDebit, nullable=True)
    bacs_debit = Column(PaymentMethodOptionsBacsDebit, nullable=True)
    bancontact = Column(PaymentMethodOptionsBancontact, nullable=True)
    blik = Column(PaymentIntentPaymentMethodOptionsBlik, nullable=True)
    boleto = Column(PaymentMethodOptionsBoleto, nullable=True)
    card = Column(PaymentIntentPaymentMethodOptionsCard, nullable=True)
    card_present = Column(PaymentMethodOptionsCardPresent, nullable=True)
    customer_balance = Column(PaymentMethodOptionsCustomerBalance, nullable=True)
    eps = Column(PaymentIntentPaymentMethodOptionsEps, nullable=True)
    fpx = Column(PaymentMethodOptionsFpx, nullable=True)
    giropay = Column(PaymentMethodOptionsGiropay, nullable=True)
    grabpay = Column(PaymentMethodOptionsGrabpay, nullable=True)
    ideal = Column(PaymentMethodOptionsIdeal, nullable=True)
    interac_present = Column(PaymentMethodOptionsInteracPresent, nullable=True)
    klarna = Column(PaymentMethodOptionsKlarna, nullable=True)
    konbini = Column(PaymentMethodOptionsKonbini, nullable=True)
    link = Column(PaymentIntentPaymentMethodOptionsLink, nullable=True)
    oxxo = Column(PaymentMethodOptionsOxxo, nullable=True)
    p24 = Column(PaymentMethodOptionsP24, nullable=True)
    paynow = Column(PaymentMethodOptionsPaynow, nullable=True)
    pix = Column(PaymentMethodOptionsPix, nullable=True)
    promptpay = Column(PaymentMethodOptionsPromptpay, nullable=True)
    sepa_debit = Column(PaymentIntentPaymentMethodOptionsSepaDebit, nullable=True)
    sofort = Column(PaymentMethodOptionsSofort, nullable=True)
    us_bank_account = Column(PaymentIntentPaymentMethodOptionsUsBankAccount, nullable=True)
    wechat_pay = Column(PaymentMethodOptionsWechatPay, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Intent_Payment_Method_Options(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, us_bank_account={us_bank_account!r}, wechat_pay={wechat_pay!r}, id={id!r})'.format(acss_debit=self.acss_debit, affirm=self.affirm, afterpay_clearpay=self.afterpay_clearpay, alipay=self.alipay, au_becs_debit=self.au_becs_debit, bacs_debit=self.bacs_debit, bancontact=self.bancontact, blik=self.blik, boleto=self.boleto, card=self.card, card_present=self.card_present, customer_balance=self.customer_balance, eps=self.eps, fpx=self.fpx, giropay=self.giropay, grabpay=self.grabpay, ideal=self.ideal, interac_present=self.interac_present, klarna=self.klarna, konbini=self.konbini, link=self.link, oxxo=self.oxxo, p24=self.p24, paynow=self.paynow, pix=self.pix, promptpay=self.promptpay, sepa_debit=self.sepa_debit, sofort=self.sofort, us_bank_account=self.us_bank_account, wechat_pay=self.wechat_pay, id=self.id)
__all__ = ['payment_intent_payment_method_options']