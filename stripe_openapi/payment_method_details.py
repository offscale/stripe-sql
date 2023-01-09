from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class PaymentMethodDetails(Base):
    __tablename__ = "payment_method_details"
    ach_credit_transfer = Column(
        String,
        ForeignKey("payment_method_details_ach_credit_transfer.bank_name"),
        nullable=True,
    )
    ach_debit = Column(
        String, ForeignKey("payment_method_details_ach_debit.bank_name"), nullable=True
    )
    acss_debit = Column(
        String, ForeignKey("payment_method_details_acss_debit.bank_name"), nullable=True
    )
    affirm = Column(
        Integer, ForeignKey("payment_method_details_affirm.id"), nullable=True
    )
    afterpay_clearpay = Column(
        Integer,
        ForeignKey("payment_method_details_afterpay_clearpay.id"),
        nullable=True,
    )
    alipay = Column(
        Integer,
        ForeignKey("payment_flows_private_payment_methods_alipay_details.id"),
        nullable=True,
    )
    au_becs_debit = Column(
        Integer, ForeignKey("payment_method_details_au_becs_debit.id"), nullable=True
    )
    bacs_debit = Column(
        Integer, ForeignKey("payment_method_details_bacs_debit.id"), nullable=True
    )
    bancontact = Column(
        Integer, ForeignKey("payment_method_details_bancontact.id"), nullable=True
    )
    blik = Column(Integer, ForeignKey("payment_method_details_blik.id"), nullable=True)
    boleto = Column(
        String, ForeignKey("payment_method_details_boleto.tax_id"), nullable=True
    )
    card = Column(Integer, ForeignKey("payment_method_details_card.id"), nullable=True)
    card_present = Column(
        String,
        ForeignKey("payment_method_details_card_present.cardholder_name"),
        nullable=True,
    )
    customer_balance = Column(
        Integer, ForeignKey("payment_method_details_customer_balance.id"), nullable=True
    )
    eps = Column(
        String, ForeignKey("payment_method_details_eps.verified_name"), nullable=True
    )
    fpx = Column(
        String, ForeignKey("payment_method_details_fpx.transaction_id"), nullable=True
    )
    giropay = Column(
        Integer, ForeignKey("payment_method_details_giropay.id"), nullable=True
    )
    grabpay = Column(
        String,
        ForeignKey("payment_method_details_grabpay.transaction_id"),
        nullable=True,
    )
    ideal = Column(
        String, ForeignKey("payment_method_details_ideal.verified_name"), nullable=True
    )
    interac_present = Column(
        String,
        ForeignKey("payment_method_details_interac_present.cardholder_name"),
        nullable=True,
    )
    klarna = Column(
        Integer, ForeignKey("payment_method_details_klarna.id"), nullable=True
    )
    konbini = Column(
        Integer, ForeignKey("payment_method_details_konbini.id"), nullable=True
    )
    link = Column(Integer, ForeignKey("payment_method_details_link.id"), nullable=True)
    multibanco = Column(
        Integer, ForeignKey("payment_method_details_multibanco.id"), nullable=True
    )
    oxxo = Column(Integer, ForeignKey("payment_method_details_oxxo.id"), nullable=True)
    p24 = Column(
        String, ForeignKey("payment_method_details_p24.verified_name"), nullable=True
    )
    paynow = Column(
        Integer, ForeignKey("payment_method_details_paynow.id"), nullable=True
    )
    pix = Column(
        String,
        ForeignKey("payment_method_details_pix.bank_transaction_id"),
        nullable=True,
    )
    promptpay = Column(
        Integer, ForeignKey("payment_method_details_promptpay.id"), nullable=True
    )
    sepa_credit_transfer = Column(
        String,
        ForeignKey("payment_method_details_sepa_credit_transfer.bank_name"),
        nullable=True,
    )
    sepa_debit = Column(
        Integer, ForeignKey("payment_method_details_sepa_debit.id"), nullable=True
    )
    sofort = Column(
        Integer, ForeignKey("payment_method_details_sofort.id"), nullable=True
    )
    stripe_account = Column(
        Integer, ForeignKey("payment_method_details_stripe_account.id"), nullable=True
    )
    type = Column(
        String,
        comment="The type of transaction-specific details of the payment method used in the payment, one of `ach_credit_transfer`, `ach_debit`, `acss_debit`, `alipay`, `au_becs_debit`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `klarna`, `multibanco`, `p24`, `sepa_debit`, `sofort`, `stripe_account`, or `wechat`.\nAn additional hash is included on `payment_method_details` with a name matching this value.\nIt contains information specific to the payment method",
    )
    us_bank_account = Column(
        String,
        ForeignKey("payment_method_details_us_bank_account.bank_name"),
        nullable=True,
    )
    wechat = Column(
        Integer, ForeignKey("payment_method_details_wechat.id"), nullable=True
    )
    wechat_pay = Column(
        String,
        ForeignKey("payment_method_details_wechat_pay.transaction_id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetails(ach_credit_transfer={ach_credit_transfer!r}, ach_debit={ach_debit!r}, acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, multibanco={multibanco!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, sepa_credit_transfer={sepa_credit_transfer!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, stripe_account={stripe_account!r}, type={type!r}, us_bank_account={us_bank_account!r}, wechat={wechat!r}, wechat_pay={wechat_pay!r}, id={id!r})".format(
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
