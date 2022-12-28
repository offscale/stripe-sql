from sqlalchemy import Column, Integer, String

class Payment_Method_Details(Base):
    __tablename__ = 'payment_method_details'
    ach_credit_transfer = Column(PaymentMethodDetailsAchCreditTransfer, nullable=True)
    ach_debit = Column(PaymentMethodDetailsAchDebit, nullable=True)
    acss_debit = Column(PaymentMethodDetailsAcssDebit, nullable=True)
    affirm = Column(PaymentMethodDetailsAffirm, nullable=True)
    afterpay_clearpay = Column(PaymentMethodDetailsAfterpayClearpay, nullable=True)
    alipay = Column(PaymentFlowsPrivatePaymentMethodsAlipayDetails, nullable=True)
    au_becs_debit = Column(PaymentMethodDetailsAuBecsDebit, nullable=True)
    bacs_debit = Column(PaymentMethodDetailsBacsDebit, nullable=True)
    bancontact = Column(PaymentMethodDetailsBancontact, nullable=True)
    blik = Column(PaymentMethodDetailsBlik, nullable=True)
    boleto = Column(PaymentMethodDetailsBoleto, nullable=True)
    card = Column(PaymentMethodDetailsCard, nullable=True)
    card_present = Column(PaymentMethodDetailsCardPresent, nullable=True)
    customer_balance = Column(PaymentMethodDetailsCustomerBalance, nullable=True)
    eps = Column(PaymentMethodDetailsEps, nullable=True)
    fpx = Column(PaymentMethodDetailsFpx, nullable=True)
    giropay = Column(PaymentMethodDetailsGiropay, nullable=True)
    grabpay = Column(PaymentMethodDetailsGrabpay, nullable=True)
    ideal = Column(PaymentMethodDetailsIdeal, nullable=True)
    interac_present = Column(PaymentMethodDetailsInteracPresent, nullable=True)
    klarna = Column(PaymentMethodDetailsKlarna, nullable=True)
    konbini = Column(PaymentMethodDetailsKonbini, nullable=True)
    link = Column(PaymentMethodDetailsLink, nullable=True)
    multibanco = Column(PaymentMethodDetailsMultibanco, nullable=True)
    oxxo = Column(PaymentMethodDetailsOxxo, nullable=True)
    p24 = Column(PaymentMethodDetailsP24, nullable=True)
    paynow = Column(PaymentMethodDetailsPaynow, nullable=True)
    pix = Column(PaymentMethodDetailsPix, nullable=True)
    promptpay = Column(PaymentMethodDetailsPromptpay, nullable=True)
    sepa_credit_transfer = Column(PaymentMethodDetailsSepaCreditTransfer, nullable=True)
    sepa_debit = Column(PaymentMethodDetailsSepaDebit, nullable=True)
    sofort = Column(PaymentMethodDetailsSofort, nullable=True)
    stripe_account = Column(PaymentMethodDetailsStripeAccount, nullable=True)
    type = Column(String, comment='The type of transaction-specific details of the payment method used in the payment, one of `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `stripe_account`, or `wechat`.\nAn additional hash is included on `payment_method_details` with a name matching this value.\nIt contains information specific to the payment method')
    us_bank_account = Column(PaymentMethodDetailsUsBankAccount, nullable=True)
    wechat = Column(PaymentMethodDetailsWechat, nullable=True)
    wechat_pay = Column(PaymentMethodDetailsWechatPay, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details(ach_credit_transfer={ach_credit_transfer!r}, ach_debit={ach_debit!r}, acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, multibanco={multibanco!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_credit_transfer={sepa_credit_transfer!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, stripe_account={stripe_account!r}, type={type!r}, us_bank_account={us_bank_account!r}, wechat={wechat!r}, wechat_pay={wechat_pay!r}, id={id!r})'.format(ach_credit_transfer=self.ach_credit_transfer, ach_debit=self.ach_debit, acss_debit=self.acss_debit, affirm=self.affirm, afterpay_clearpay=self.afterpay_clearpay, alipay=self.alipay, au_becs_debit=self.au_becs_debit, bacs_debit=self.bacs_debit, bancontact=self.bancontact, blik=self.blik, boleto=self.boleto, card=self.card, card_present=self.card_present, customer_balance=self.customer_balance, eps=self.eps, fpx=self.fpx, giropay=self.giropay, grabpay=self.grabpay, ideal=self.ideal, interac_present=self.interac_present, klarna=self.klarna, konbini=self.konbini, link=self.link, multibanco=self.multibanco, oxxo=self.oxxo, p24=self.p24, paynow=self.paynow, pix=self.pix, promptpay=self.promptpay, sepa_credit_transfer=self.sepa_credit_transfer, sepa_debit=self.sepa_debit, sofort=self.sofort, stripe_account=self.stripe_account, type=self.type, us_bank_account=self.us_bank_account, wechat=self.wechat, wechat_pay=self.wechat_pay, id=self.id)
__all__ = ['payment_method_details']