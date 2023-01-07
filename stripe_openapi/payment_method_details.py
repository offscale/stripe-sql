from sqlalchemy import Column, Integer, String


class Payment_Method_Details(Base):
    __tablename__ = "payment_method_details"
    ach_credit_transfer = Column(
        payment_method_details_ach_credit_transfer,
        ForeignKey("payment_method_details_ach_credit_transfer"),
        nullable=True,
    )
    ach_debit = Column(
        payment_method_details_ach_debit,
        ForeignKey("payment_method_details_ach_debit"),
        nullable=True,
    )
    acss_debit = Column(
        payment_method_details_acss_debit,
        ForeignKey("payment_method_details_acss_debit"),
        nullable=True,
    )
    affirm = Column(
        payment_method_details_affirm,
        ForeignKey("payment_method_details_affirm"),
        nullable=True,
    )
    afterpay_clearpay = Column(
        payment_method_details_afterpay_clearpay,
        ForeignKey("payment_method_details_afterpay_clearpay"),
        nullable=True,
    )
    alipay = Column(
        payment_flows_private_payment_methods_alipay_details,
        ForeignKey("payment_flows_private_payment_methods_alipay_details"),
        nullable=True,
    )
    au_becs_debit = Column(
        payment_method_details_au_becs_debit,
        ForeignKey("payment_method_details_au_becs_debit"),
        nullable=True,
    )
    bacs_debit = Column(
        payment_method_details_bacs_debit,
        ForeignKey("payment_method_details_bacs_debit"),
        nullable=True,
    )
    bancontact = Column(
        payment_method_details_bancontact,
        ForeignKey("payment_method_details_bancontact"),
        nullable=True,
    )
    blik = Column(
        payment_method_details_blik,
        ForeignKey("payment_method_details_blik"),
        nullable=True,
    )
    boleto = Column(
        payment_method_details_boleto,
        ForeignKey("payment_method_details_boleto"),
        nullable=True,
    )
    card = Column(
        payment_method_details_card,
        ForeignKey("payment_method_details_card"),
        nullable=True,
    )
    card_present = Column(
        payment_method_details_card_present,
        ForeignKey("payment_method_details_card_present"),
        nullable=True,
    )
    customer_balance = Column(
        payment_method_details_customer_balance,
        ForeignKey("payment_method_details_customer_balance"),
        nullable=True,
    )
    eps = Column(
        payment_method_details_eps,
        ForeignKey("payment_method_details_eps"),
        nullable=True,
    )
    fpx = Column(
        payment_method_details_fpx,
        ForeignKey("payment_method_details_fpx"),
        nullable=True,
    )
    giropay = Column(
        payment_method_details_giropay,
        ForeignKey("payment_method_details_giropay"),
        nullable=True,
    )
    grabpay = Column(
        payment_method_details_grabpay,
        ForeignKey("payment_method_details_grabpay"),
        nullable=True,
    )
    ideal = Column(
        payment_method_details_ideal,
        ForeignKey("payment_method_details_ideal"),
        nullable=True,
    )
    interac_present = Column(
        payment_method_details_interac_present,
        ForeignKey("payment_method_details_interac_present"),
        nullable=True,
    )
    klarna = Column(
        payment_method_details_klarna,
        ForeignKey("payment_method_details_klarna"),
        nullable=True,
    )
    konbini = Column(
        payment_method_details_konbini,
        ForeignKey("payment_method_details_konbini"),
        nullable=True,
    )
    link = Column(
        payment_method_details_link,
        ForeignKey("payment_method_details_link"),
        nullable=True,
    )
    multibanco = Column(
        payment_method_details_multibanco,
        ForeignKey("payment_method_details_multibanco"),
        nullable=True,
    )
    oxxo = Column(
        payment_method_details_oxxo,
        ForeignKey("payment_method_details_oxxo"),
        nullable=True,
    )
    p24 = Column(
        payment_method_details_p24,
        ForeignKey("payment_method_details_p24"),
        nullable=True,
    )
    paynow = Column(
        payment_method_details_paynow,
        ForeignKey("payment_method_details_paynow"),
        nullable=True,
    )
    pix = Column(
        payment_method_details_pix,
        ForeignKey("payment_method_details_pix"),
        nullable=True,
    )
    promptpay = Column(
        payment_method_details_promptpay,
        ForeignKey("payment_method_details_promptpay"),
        nullable=True,
    )
    sepa_credit_transfer = Column(
        payment_method_details_sepa_credit_transfer,
        ForeignKey("payment_method_details_sepa_credit_transfer"),
        nullable=True,
    )
    sepa_debit = Column(
        payment_method_details_sepa_debit,
        ForeignKey("payment_method_details_sepa_debit"),
        nullable=True,
    )
    sofort = Column(
        payment_method_details_sofort,
        ForeignKey("payment_method_details_sofort"),
        nullable=True,
    )
    stripe_account = Column(
        payment_method_details_stripe_account,
        ForeignKey("payment_method_details_stripe_account"),
        nullable=True,
    )
    type = Column(
        String,
        comment="The type of transaction-specific details of the payment method used in the payment, one of `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `stripe_account`, or `wechat`.\nAn additional hash is included on `payment_method_details` with a name matching this value.\nIt contains information specific to the payment method",
    )
    us_bank_account = Column(
        payment_method_details_us_bank_account,
        ForeignKey("payment_method_details_us_bank_account"),
        nullable=True,
    )
    wechat = Column(
        payment_method_details_wechat,
        ForeignKey("payment_method_details_wechat"),
        nullable=True,
    )
    wechat_pay = Column(
        payment_method_details_wechat_pay,
        ForeignKey("payment_method_details_wechat_pay"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details(ach_credit_transfer={ach_credit_transfer!r}, ach_debit={ach_debit!r}, acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, multibanco={multibanco!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_credit_transfer={sepa_credit_transfer!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, stripe_account={stripe_account!r}, type={type!r}, us_bank_account={us_bank_account!r}, wechat={wechat!r}, wechat_pay={wechat_pay!r}, id={id!r})".format(
            ach_credit_transfer=self.ach_credit_transfer,
            ach_debit=self.ach_debit,
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
            multibanco=self.multibanco,
            oxxo=self.oxxo,
            p24=self.p24,
            paynow=self.paynow,
            pix=self.pix,
            promptpay=self.promptpay,
            sepa_credit_transfer=self.sepa_credit_transfer,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            stripe_account=self.stripe_account,
            type=self.type,
            us_bank_account=self.us_bank_account,
            wechat=self.wechat,
            wechat_pay=self.wechat_pay,
            id=self.id,
        )


__all__ = ["payment_method_details"]
