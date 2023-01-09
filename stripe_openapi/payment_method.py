from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class PaymentMethod(Base):
    """
    PaymentMethod objects represent your customer's payment instruments.

    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).

    """

    __tablename__ = "payment_method"
    acss_debit = Column(
        String, ForeignKey("payment_method_acss_debit.bank_name"), nullable=True
    )
    affirm = Column(Integer, ForeignKey("payment_method_affirm.id"), nullable=True)
    afterpay_clearpay = Column(
        Integer, ForeignKey("payment_method_afterpay_clearpay.id"), nullable=True
    )
    alipay = Column(
        Integer,
        ForeignKey("payment_flows_private_payment_methods_alipay.id"),
        nullable=True,
    )
    au_becs_debit = Column(
        Integer, ForeignKey("payment_method_au_becs_debit.id"), nullable=True
    )
    bacs_debit = Column(
        Integer, ForeignKey("payment_method_bacs_debit.id"), nullable=True
    )
    bancontact = Column(
        Integer, ForeignKey("payment_method_bancontact.id"), nullable=True
    )
    billing_details = Column(Integer, ForeignKey("billing_details.id"))
    blik = Column(Integer, ForeignKey("payment_method_blik.id"), nullable=True)
    boleto = Column(String, ForeignKey("payment_method_boleto.tax_id"), nullable=True)
    card = Column(Integer, ForeignKey("payment_method_card.id"), nullable=True)
    card_present = Column(
        Integer, ForeignKey("payment_method_card_present.id"), nullable=True
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        Customer,
        comment="[[FK(Customer)]] The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer",
        nullable=True,
    )
    customer_balance = Column(
        Integer, ForeignKey("payment_method_customer_balance.id"), nullable=True
    )
    eps = Column(Integer, ForeignKey("payment_method_eps.id"), nullable=True)
    fpx = Column(Integer, ForeignKey("payment_method_fpx.id"), nullable=True)
    giropay = Column(Integer, ForeignKey("payment_method_giropay.id"), nullable=True)
    grabpay = Column(Integer, ForeignKey("payment_method_grabpay.id"), nullable=True)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    ideal = Column(Integer, ForeignKey("payment_method_ideal.id"), nullable=True)
    interac_present = Column(
        Integer, ForeignKey("payment_method_interac_present.id"), nullable=True
    )
    klarna = Column(Integer, ForeignKey("payment_method_klarna.id"), nullable=True)
    konbini = Column(Integer, ForeignKey("payment_method_konbini.id"), nullable=True)
    link = Column(Integer, ForeignKey("payment_method_link.id"), nullable=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    oxxo = Column(Integer, ForeignKey("payment_method_oxxo.id"), nullable=True)
    p24 = Column(Integer, ForeignKey("payment_method_p24.id"), nullable=True)
    paynow = Column(Integer, ForeignKey("payment_method_paynow.id"), nullable=True)
    pix = Column(Integer, ForeignKey("payment_method_pix.id"), nullable=True)
    promptpay = Column(
        Integer, ForeignKey("payment_method_promptpay.id"), nullable=True
    )
    radar_options = Column(Integer, ForeignKey("radar_radar_options.id"), nullable=True)
    sepa_debit = Column(
        Integer, ForeignKey("payment_method_sepa_debit.id"), nullable=True
    )
    sofort = Column(Integer, ForeignKey("payment_method_sofort.id"), nullable=True)
    type = Column(
        String,
        comment="The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type",
    )
    us_bank_account = Column(
        String, ForeignKey("payment_method_us_bank_account.bank_name"), nullable=True
    )
    wechat_pay = Column(
        Integer, ForeignKey("payment_method_wechat_pay.id"), nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethod(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, billing_details={billing_details!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, created={created!r}, customer={customer!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, id={id!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, radar_options={radar_options!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, type={type!r}, us_bank_account={us_bank_account!r}, wechat_pay={wechat_pay!r})".format(
            acss_debit=self.acss_debit,
            affirm=self.affirm,
            afterpay_clearpay=self.afterpay_clearpay,
            alipay=self.alipay,
            au_becs_debit=self.au_becs_debit,
            bacs_debit=self.bacs_debit,
            bancontact=self.bancontact,
            billing_details=self.billing_details,
            blik=self.blik,
            boleto=self.boleto,
            card=self.card,
            card_present=self.card_present,
            created=self.created,
            customer=self.customer,
            customer_balance=self.customer_balance,
            eps=self.eps,
            fpx=self.fpx,
            giropay=self.giropay,
            grabpay=self.grabpay,
            id=self.id,
            ideal=self.ideal,
            interac_present=self.interac_present,
            klarna=self.klarna,
            konbini=self.konbini,
            link=self.link,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            oxxo=self.oxxo,
            p24=self.p24,
            paynow=self.paynow,
            pix=self.pix,
            promptpay=self.promptpay,
            radar_options=self.radar_options,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            type=self.type,
            us_bank_account=self.us_bank_account,
            wechat_pay=self.wechat_pay,
        )


__all__ = ["payment_method"]
