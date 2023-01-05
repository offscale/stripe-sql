from sqlalchemy import Boolean, Column, Integer, String


class Payment_Method(Base):
    """
    PaymentMethod objects represent your customer's payment instruments.

    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).

    """

    __tablename__ = "payment_method"
    acss_debit = Column(PaymentMethodAcssDebit, nullable=True)
    affirm = Column(PaymentMethodAffirm, nullable=True)
    afterpay_clearpay = Column(PaymentMethodAfterpayClearpay, nullable=True)
    alipay = Column(PaymentFlowsPrivatePaymentMethodsAlipay, nullable=True)
    au_becs_debit = Column(PaymentMethodAuBecsDebit, nullable=True)
    bacs_debit = Column(PaymentMethodBacsDebit, nullable=True)
    bancontact = Column(PaymentMethodBancontact, nullable=True)
    billing_details = Column(BillingDetails)
    blik = Column(PaymentMethodBlik, nullable=True)
    boleto = Column(PaymentMethodBoleto, nullable=True)
    card = Column(PaymentMethodCard, nullable=True)
    card_present = Column(PaymentMethodCardPresent, nullable=True)
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        Customer,
        comment="The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer",
        nullable=True,
    )
    customer_balance = Column(PaymentMethodCustomerBalance, nullable=True)
    eps = Column(PaymentMethodEps, nullable=True)
    fpx = Column(PaymentMethodFpx, nullable=True)
    giropay = Column(PaymentMethodGiropay, nullable=True)
    grabpay = Column(PaymentMethodGrabpay, nullable=True)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    ideal = Column(PaymentMethodIdeal, nullable=True)
    interac_present = Column(PaymentMethodInteracPresent, nullable=True)
    klarna = Column(PaymentMethodKlarna, nullable=True)
    konbini = Column(PaymentMethodKonbini, nullable=True)
    link = Column(PaymentMethodLink, nullable=True)
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
    oxxo = Column(PaymentMethodOxxo, nullable=True)
    p24 = Column(PaymentMethodP24, nullable=True)
    paynow = Column(PaymentMethodPaynow, nullable=True)
    pix = Column(PaymentMethodPix, nullable=True)
    promptpay = Column(PaymentMethodPromptpay, nullable=True)
    radar_options = Column(RadarRadarOptions, nullable=True)
    sepa_debit = Column(PaymentMethodSepaDebit, nullable=True)
    sofort = Column(PaymentMethodSofort, nullable=True)
    type = Column(
        String,
        comment="The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type",
    )
    us_bank_account = Column(PaymentMethodUsBankAccount, nullable=True)
    wechat_pay = Column(PaymentMethodWechatPay, nullable=True)

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
