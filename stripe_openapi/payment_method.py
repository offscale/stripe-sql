from sqlalchemy import Boolean, Column, Integer, String


class Payment_Method(Base):
    """
    PaymentMethod objects represent your customer's payment instruments.

    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).

    """

    __tablename__ = "payment_method"
    acss_debit = Column(
        payment_method_acss_debit,
        ForeignKey("payment_method_acss_debit"),
        nullable=True,
    )
    affirm = Column(
        payment_method_affirm, ForeignKey("payment_method_affirm"), nullable=True
    )
    afterpay_clearpay = Column(
        payment_method_afterpay_clearpay,
        ForeignKey("payment_method_afterpay_clearpay"),
        nullable=True,
    )
    alipay = Column(
        payment_flows_private_payment_methods_alipay,
        ForeignKey("payment_flows_private_payment_methods_alipay"),
        nullable=True,
    )
    au_becs_debit = Column(
        payment_method_au_becs_debit,
        ForeignKey("payment_method_au_becs_debit"),
        nullable=True,
    )
    bacs_debit = Column(
        payment_method_bacs_debit,
        ForeignKey("payment_method_bacs_debit"),
        nullable=True,
    )
    bancontact = Column(
        payment_method_bancontact,
        ForeignKey("payment_method_bancontact"),
        nullable=True,
    )
    billing_details = Column(billing_details, ForeignKey("billing_details"))
    blik = Column(payment_method_blik, ForeignKey("payment_method_blik"), nullable=True)
    boleto = Column(
        payment_method_boleto, ForeignKey("payment_method_boleto"), nullable=True
    )
    card = Column(payment_method_card, ForeignKey("payment_method_card"), nullable=True)
    card_present = Column(
        payment_method_card_present,
        ForeignKey("payment_method_card_present"),
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        customer,
        comment="[[FK(customer)]] The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer",
        nullable=True,
    )
    customer_balance = Column(
        payment_method_customer_balance,
        ForeignKey("payment_method_customer_balance"),
        nullable=True,
    )
    eps = Column(payment_method_eps, ForeignKey("payment_method_eps"), nullable=True)
    fpx = Column(payment_method_fpx, ForeignKey("payment_method_fpx"), nullable=True)
    giropay = Column(
        payment_method_giropay, ForeignKey("payment_method_giropay"), nullable=True
    )
    grabpay = Column(
        payment_method_grabpay, ForeignKey("payment_method_grabpay"), nullable=True
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    ideal = Column(
        payment_method_ideal, ForeignKey("payment_method_ideal"), nullable=True
    )
    interac_present = Column(
        payment_method_interac_present,
        ForeignKey("payment_method_interac_present"),
        nullable=True,
    )
    klarna = Column(
        payment_method_klarna, ForeignKey("payment_method_klarna"), nullable=True
    )
    konbini = Column(
        payment_method_konbini, ForeignKey("payment_method_konbini"), nullable=True
    )
    link = Column(payment_method_link, ForeignKey("payment_method_link"), nullable=True)
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
    oxxo = Column(payment_method_oxxo, ForeignKey("payment_method_oxxo"), nullable=True)
    p24 = Column(payment_method_p24, ForeignKey("payment_method_p24"), nullable=True)
    paynow = Column(
        payment_method_paynow, ForeignKey("payment_method_paynow"), nullable=True
    )
    pix = Column(payment_method_pix, ForeignKey("payment_method_pix"), nullable=True)
    promptpay = Column(
        payment_method_promptpay, ForeignKey("payment_method_promptpay"), nullable=True
    )
    radar_options = Column(
        radar_radar_options, ForeignKey("radar_radar_options"), nullable=True
    )
    sepa_debit = Column(
        payment_method_sepa_debit,
        ForeignKey("payment_method_sepa_debit"),
        nullable=True,
    )
    sofort = Column(
        payment_method_sofort, ForeignKey("payment_method_sofort"), nullable=True
    )
    type = Column(
        String,
        comment="The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type",
    )
    us_bank_account = Column(
        payment_method_us_bank_account,
        ForeignKey("payment_method_us_bank_account"),
        nullable=True,
    )
    wechat_pay = Column(
        payment_method_wechat_pay,
        ForeignKey("payment_method_wechat_pay"),
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method(acss_debit={acss_debit!r}, affirm={affirm!r}, afterpay_clearpay={afterpay_clearpay!r}, alipay={alipay!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, billing_details={billing_details!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, created={created!r}, customer={customer!r}, customer_balance={customer_balance!r}, eps={eps!r}, fpx={fpx!r}, giropay={giropay!r}, grabpay={grabpay!r}, id={id!r}, ideal={ideal!r}, interac_present={interac_present!r}, klarna={klarna!r}, konbini={konbini!r}, link={link!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, oxxo={oxxo!r}, p24={p24!r}, paynow={paynow!r}, pix={pix!r}, promptpay={promptpay!r}, radar_options={radar_options!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, type={type!r}, us_bank_account={us_bank_account!r}, wechat_pay={wechat_pay!r})".format(
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
