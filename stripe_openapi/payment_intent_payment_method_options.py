from sqlalchemy import Column, Integer


class Payment_Intent_Payment_Method_Options(Base):
    __tablename__ = "payment_intent_payment_method_options"
    acss_debit = Column(
        payment_intent_payment_method_options_acss_debit,
        ForeignKey("payment_intent_payment_method_options_acss_debit"),
        nullable=True,
    )
    affirm = Column(
        payment_method_options_affirm,
        ForeignKey("payment_method_options_affirm"),
        nullable=True,
    )
    afterpay_clearpay = Column(
        payment_method_options_afterpay_clearpay,
        ForeignKey("payment_method_options_afterpay_clearpay"),
        nullable=True,
    )
    alipay = Column(
        payment_method_options_alipay,
        ForeignKey("payment_method_options_alipay"),
        nullable=True,
    )
    au_becs_debit = Column(
        payment_intent_payment_method_options_au_becs_debit,
        ForeignKey("payment_intent_payment_method_options_au_becs_debit"),
        nullable=True,
    )
    bacs_debit = Column(
        payment_method_options_bacs_debit,
        ForeignKey("payment_method_options_bacs_debit"),
        nullable=True,
    )
    bancontact = Column(
        payment_method_options_bancontact,
        ForeignKey("payment_method_options_bancontact"),
        nullable=True,
    )
    blik = Column(
        payment_intent_payment_method_options_blik,
        ForeignKey("payment_intent_payment_method_options_blik"),
        nullable=True,
    )
    boleto = Column(
        payment_method_options_boleto,
        ForeignKey("payment_method_options_boleto"),
        nullable=True,
    )
    card = Column(
        payment_intent_payment_method_options_card,
        ForeignKey("payment_intent_payment_method_options_card"),
        nullable=True,
    )
    card_present = Column(
        payment_method_options_card_present,
        ForeignKey("payment_method_options_card_present"),
        nullable=True,
    )
    customer_balance = Column(
        payment_method_options_customer_balance,
        ForeignKey("payment_method_options_customer_balance"),
        nullable=True,
    )
    eps = Column(
        payment_intent_payment_method_options_eps,
        ForeignKey("payment_intent_payment_method_options_eps"),
        nullable=True,
    )
    fpx = Column(
        payment_method_options_fpx,
        ForeignKey("payment_method_options_fpx"),
        nullable=True,
    )
    giropay = Column(
        payment_method_options_giropay,
        ForeignKey("payment_method_options_giropay"),
        nullable=True,
    )
    grabpay = Column(
        payment_method_options_grabpay,
        ForeignKey("payment_method_options_grabpay"),
        nullable=True,
    )
    ideal = Column(
        payment_method_options_ideal,
        ForeignKey("payment_method_options_ideal"),
        nullable=True,
    )
    interac_present = Column(
        payment_method_options_interac_present,
        ForeignKey("payment_method_options_interac_present"),
        nullable=True,
    )
    klarna = Column(
        payment_method_options_klarna,
        ForeignKey("payment_method_options_klarna"),
        nullable=True,
    )
    konbini = Column(
        payment_method_options_konbini,
        ForeignKey("payment_method_options_konbini"),
        nullable=True,
    )
    link = Column(
        payment_intent_payment_method_options_link,
        ForeignKey("payment_intent_payment_method_options_link"),
        nullable=True,
    )
    oxxo = Column(
        payment_method_options_oxxo,
        ForeignKey("payment_method_options_oxxo"),
        nullable=True,
    )
    p24 = Column(
        payment_method_options_p24,
        ForeignKey("payment_method_options_p24"),
        nullable=True,
    )
    paynow = Column(
        payment_method_options_paynow,
        ForeignKey("payment_method_options_paynow"),
        nullable=True,
    )
    pix = Column(
        payment_method_options_pix,
        ForeignKey("payment_method_options_pix"),
        nullable=True,
    )
    promptpay = Column(
        payment_method_options_promptpay,
        ForeignKey("payment_method_options_promptpay"),
        nullable=True,
    )
    sepa_debit = Column(
        payment_intent_payment_method_options_sepa_debit,
        ForeignKey("payment_intent_payment_method_options_sepa_debit"),
        nullable=True,
    )
    sofort = Column(
        payment_method_options_sofort,
        ForeignKey("payment_method_options_sofort"),
        nullable=True,
    )
    us_bank_account = Column(
        payment_intent_payment_method_options_us_bank_account,
        ForeignKey("payment_intent_payment_method_options_us_bank_account"),
        nullable=True,
    )
    wechat_pay = Column(
        payment_method_options_wechat_pay,
        ForeignKey("payment_method_options_wechat_pay"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Payment_Method_Options(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, us_bank_account={us_bank_account!r}, wechat_pay={wechat_pay!r}, id={id!r})".format(
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
