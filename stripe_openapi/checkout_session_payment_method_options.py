from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class CheckoutSessionPaymentMethodOptions(Base):
    __tablename__ = "checkout_session_payment_method_options"
    acss_debit = Column(
        Integer,
        ForeignKey("checkout_acss_debit_payment_method_options.id"),
        nullable=True,
    )
    affirm = Column(
        Integer, ForeignKey("checkout_affirm_payment_method_options.id"), nullable=True
    )
    afterpay_clearpay = Column(
        Integer,
        ForeignKey("checkout_afterpay_clearpay_payment_method_options.id"),
        nullable=True,
    )
    alipay = Column(
        Integer, ForeignKey("checkout_alipay_payment_method_options.id"), nullable=True
    )
    au_becs_debit = Column(
        Integer,
        ForeignKey("checkout_au_becs_debit_payment_method_options.id"),
        nullable=True,
    )
    bacs_debit = Column(
        Integer,
        ForeignKey("checkout_bacs_debit_payment_method_options.id"),
        nullable=True,
    )
    bancontact = Column(
        Integer,
        ForeignKey("checkout_bancontact_payment_method_options.id"),
        nullable=True,
    )
    boleto = Column(
        Integer, ForeignKey("checkout_boleto_payment_method_options.id"), nullable=True
    )
    card = Column(
        Integer, ForeignKey("checkout_card_payment_method_options.id"), nullable=True
    )
    customer_balance = Column(
        Integer,
        ForeignKey("checkout_customer_balance_payment_method_options.id"),
        nullable=True,
    )
    eps = Column(
        Integer, ForeignKey("checkout_eps_payment_method_options.id"), nullable=True
    )
    fpx = Column(
        Integer, ForeignKey("checkout_fpx_payment_method_options.id"), nullable=True
    )
    giropay = Column(
        Integer, ForeignKey("checkout_giropay_payment_method_options.id"), nullable=True
    )
    grabpay = Column(
        Integer,
        ForeignKey("checkout_grab_pay_payment_method_options.id"),
        nullable=True,
    )
    ideal = Column(
        Integer, ForeignKey("checkout_ideal_payment_method_options.id"), nullable=True
    )
    klarna = Column(
        Integer, ForeignKey("checkout_klarna_payment_method_options.id"), nullable=True
    )
    konbini = Column(
        Integer, ForeignKey("checkout_konbini_payment_method_options.id"), nullable=True
    )
    oxxo = Column(
        Integer, ForeignKey("checkout_oxxo_payment_method_options.id"), nullable=True
    )
    p24 = Column(
        Integer, ForeignKey("checkout_p24_payment_method_options.id"), nullable=True
    )
    paynow = Column(
        Integer, ForeignKey("checkout_paynow_payment_method_options.id"), nullable=True
    )
    pix = Column(
        Integer, ForeignKey("checkout_pix_payment_method_options.id"), nullable=True
    )
    sepa_debit = Column(
        Integer,
        ForeignKey("checkout_sepa_debit_payment_method_options.id"),
        nullable=True,
    )
    sofort = Column(
        Integer, ForeignKey("checkout_sofort_payment_method_options.id"), nullable=True
    )
    us_bank_account = Column(
        Integer,
        ForeignKey("checkout_us_bank_account_payment_method_options.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CheckoutSessionPaymentMethodOptions(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, boleto={boleto!r}, card={card!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, klarna={klarna!r}, konbini={konbini!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
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
