from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentIntentPaymentMethodOptions(Base):
    __tablename__ = "payment_intent_payment_method_options"
    acss_debit = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_acss_debit.id"),
        nullable=True,
    )
    affirm = Column(
        Integer, ForeignKey("payment_method_options_affirm.id"), nullable=True
    )
    afterpay_clearpay = Column(
        Integer,
        ForeignKey("payment_method_options_afterpay_clearpay.id"),
        nullable=True,
    )
    alipay = Column(
        Integer, ForeignKey("payment_method_options_alipay.id"), nullable=True
    )
    au_becs_debit = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_au_becs_debit.id"),
        nullable=True,
    )
    bacs_debit = Column(
        Integer, ForeignKey("payment_method_options_bacs_debit.id"), nullable=True
    )
    bancontact = Column(
        Integer, ForeignKey("payment_method_options_bancontact.id"), nullable=True
    )
    blik = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_blik.id"),
        nullable=True,
    )
    boleto = Column(
        Integer, ForeignKey("payment_method_options_boleto.id"), nullable=True
    )
    card = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_card.id"),
        nullable=True,
    )
    card_present = Column(
        Integer, ForeignKey("payment_method_options_card_present.id"), nullable=True
    )
    customer_balance = Column(
        Integer, ForeignKey("payment_method_options_customer_balance.id"), nullable=True
    )
    eps = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_eps.id"),
        nullable=True,
    )
    fpx = Column(Integer, ForeignKey("payment_method_options_fpx.id"), nullable=True)
    giropay = Column(
        Integer, ForeignKey("payment_method_options_giropay.id"), nullable=True
    )
    grabpay = Column(
        Integer, ForeignKey("payment_method_options_grabpay.id"), nullable=True
    )
    ideal = Column(
        Integer, ForeignKey("payment_method_options_ideal.id"), nullable=True
    )
    interac_present = Column(
        Integer, ForeignKey("payment_method_options_interac_present.id"), nullable=True
    )
    klarna = Column(
        Integer, ForeignKey("payment_method_options_klarna.id"), nullable=True
    )
    konbini = Column(
        Integer, ForeignKey("payment_method_options_konbini.id"), nullable=True
    )
    link = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_link.id"),
        nullable=True,
    )
    oxxo = Column(Integer, ForeignKey("payment_method_options_oxxo.id"), nullable=True)
    p24 = Column(Integer, ForeignKey("payment_method_options_p24.id"), nullable=True)
    paynow = Column(
        Integer, ForeignKey("payment_method_options_paynow.id"), nullable=True
    )
    pix = Column(Integer, ForeignKey("payment_method_options_pix.id"), nullable=True)
    promptpay = Column(
        Integer, ForeignKey("payment_method_options_promptpay.id"), nullable=True
    )
    sepa_debit = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_sepa_debit.id"),
        nullable=True,
    )
    sofort = Column(
        Integer, ForeignKey("payment_method_options_sofort.id"), nullable=True
    )
    us_bank_account = Column(
        Integer,
        ForeignKey("payment_intent_payment_method_options_us_bank_account.id"),
        nullable=True,
    )
    wechat_pay = Column(
        String, ForeignKey("payment_method_options_wechat_pay.app_id"), nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentPaymentMethodOptions(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, us_bank_account={us_bank_account!r}, wechat_pay={wechat_pay!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            affirm=self.affirm,
            afterpay_clearpay=self.afterpay_clearpay,
            alipay=self.alipay,
            au_becs_debit=self.au_becs_debit,
            bacs_debit=self.bacs_debit,
            bancontact=self.bancontact,
            blik=self.blik,
            boleto=self.boleto,
            card=self.card,
            card_present=self.card_present,
            customer_balance=self.customer_balance,
            eps=self.eps,
            fpx=self.fpx,
            giropay=self.giropay,
            grabpay=self.grabpay,
            ideal=self.ideal,
            interac_present=self.interac_present,
            klarna=self.klarna,
            konbini=self.konbini,
            link=self.link,
            oxxo=self.oxxo,
            p24=self.p24,
            paynow=self.paynow,
            pix=self.pix,
            promptpay=self.promptpay,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            us_bank_account=self.us_bank_account,
            wechat_pay=self.wechat_pay,
            id=self.id,
        )


__all__ = ["payment_intent_payment_method_options"]
