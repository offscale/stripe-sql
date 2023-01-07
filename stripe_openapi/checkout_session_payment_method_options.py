from sqlalchemy import Column, Integer


class Checkout_Session_Payment_Method_Options(Base):
    __tablename__ = "checkout_session_payment_method_options"
    acss_debit = Column(
        checkout_acss_debit_payment_method_options,
        ForeignKey("checkout_acss_debit_payment_method_options"),
        nullable=True,
    )
    affirm = Column(
        checkout_affirm_payment_method_options,
        ForeignKey("checkout_affirm_payment_method_options"),
        nullable=True,
    )
    afterpay_clearpay = Column(
        checkout_afterpay_clearpay_payment_method_options,
        ForeignKey("checkout_afterpay_clearpay_payment_method_options"),
        nullable=True,
    )
    alipay = Column(
        checkout_alipay_payment_method_options,
        ForeignKey("checkout_alipay_payment_method_options"),
        nullable=True,
    )
    au_becs_debit = Column(
        checkout_au_becs_debit_payment_method_options,
        ForeignKey("checkout_au_becs_debit_payment_method_options"),
        nullable=True,
    )
    bacs_debit = Column(
        checkout_bacs_debit_payment_method_options,
        ForeignKey("checkout_bacs_debit_payment_method_options"),
        nullable=True,
    )
    bancontact = Column(
        checkout_bancontact_payment_method_options,
        ForeignKey("checkout_bancontact_payment_method_options"),
        nullable=True,
    )
    boleto = Column(
        checkout_boleto_payment_method_options,
        ForeignKey("checkout_boleto_payment_method_options"),
        nullable=True,
    )
    card = Column(
        checkout_card_payment_method_options,
        ForeignKey("checkout_card_payment_method_options"),
        nullable=True,
    )
    customer_balance = Column(
        checkout_customer_balance_payment_method_options,
        ForeignKey("checkout_customer_balance_payment_method_options"),
        nullable=True,
    )
    eps = Column(
        checkout_eps_payment_method_options,
        ForeignKey("checkout_eps_payment_method_options"),
        nullable=True,
    )
    fpx = Column(
        checkout_fpx_payment_method_options,
        ForeignKey("checkout_fpx_payment_method_options"),
        nullable=True,
    )
    giropay = Column(
        checkout_giropay_payment_method_options,
        ForeignKey("checkout_giropay_payment_method_options"),
        nullable=True,
    )
    grabpay = Column(
        checkout_grab_pay_payment_method_options,
        ForeignKey("checkout_grab_pay_payment_method_options"),
        nullable=True,
    )
    ideal = Column(
        checkout_ideal_payment_method_options,
        ForeignKey("checkout_ideal_payment_method_options"),
        nullable=True,
    )
    klarna = Column(
        checkout_klarna_payment_method_options,
        ForeignKey("checkout_klarna_payment_method_options"),
        nullable=True,
    )
    konbini = Column(
        checkout_konbini_payment_method_options,
        ForeignKey("checkout_konbini_payment_method_options"),
        nullable=True,
    )
    oxxo = Column(
        checkout_oxxo_payment_method_options,
        ForeignKey("checkout_oxxo_payment_method_options"),
        nullable=True,
    )
    p24 = Column(
        checkout_p24_payment_method_options,
        ForeignKey("checkout_p24_payment_method_options"),
        nullable=True,
    )
    paynow = Column(
        checkout_paynow_payment_method_options,
        ForeignKey("checkout_paynow_payment_method_options"),
        nullable=True,
    )
    pix = Column(
        checkout_pix_payment_method_options,
        ForeignKey("checkout_pix_payment_method_options"),
        nullable=True,
    )
    sepa_debit = Column(
        checkout_sepa_debit_payment_method_options,
        ForeignKey("checkout_sepa_debit_payment_method_options"),
        nullable=True,
    )
    sofort = Column(
        checkout_sofort_payment_method_options,
        ForeignKey("checkout_sofort_payment_method_options"),
        nullable=True,
    )
    us_bank_account = Column(
        checkout_us_bank_account_payment_method_options,
        ForeignKey("checkout_us_bank_account_payment_method_options"),
        nullable=True,
    )
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
