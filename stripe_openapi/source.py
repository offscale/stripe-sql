from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String

from stripe_openapi.source_owner import SourceOwner

from . import Base


class Source(Base):
    """
    `Source` objects allow you to accept a variety of payment methods. They

    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
    This newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).

    """

    __tablename__ = "source"
    ach_credit_transfer = Column(
        Integer, ForeignKey("source_type_ach_credit_transfer.id"), nullable=True
    )
    ach_debit = Column(
        String, ForeignKey("source_type_ach_debit.bank_name"), nullable=True
    )
    acss_debit = Column(
        String, ForeignKey("source_type_acss_debit.bank_name"), nullable=True
    )
    alipay = Column(Integer, ForeignKey("source_type_alipay.id"), nullable=True)
    amount = Column(
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources",
        nullable=True,
    )
    au_becs_debit = Column(
        Integer, ForeignKey("source_type_au_becs_debit.id"), nullable=True
    )
    bancontact = Column(
        String, ForeignKey("source_type_bancontact.bank_name"), nullable=True
    )
    card = Column(Integer, ForeignKey("source_type_card.id"), nullable=True)
    card_present = Column(
        Integer, ForeignKey("source_type_card_present.id"), nullable=True
    )
    client_secret = Column(
        String,
        comment="The client secret of the source. Used for client-side retrieval using a publishable key",
    )
    code_verification = Column(
        Integer, ForeignKey("source_code_verification_flow.id"), nullable=True
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources",
        nullable=True,
    )
    customer = Column(
        String,
        comment="The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer",
        nullable=True,
    )
    eps = Column(Integer, ForeignKey("source_type_eps.id"), nullable=True)
    flow = Column(
        String,
        comment="The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`",
    )
    giropay = Column(String, ForeignKey("source_type_giropay.bank_name"), nullable=True)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    ideal = Column(Integer, ForeignKey("source_type_ideal.id"), nullable=True)
    klarna = Column(Integer, ForeignKey("source_type_klarna.id"), nullable=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    multibanco = Column(
        String,
        ForeignKey("source_type_multibanco.refund_account_holder_name"),
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    owner = Column(
        SourceOwner,
        comment="[[FK(SourceOwner)]] Information about the owner of the payment instrument that may be used or required by particular source types",
        nullable=True,
    )
    p24 = Column(Integer, ForeignKey("source_type_p24.id"), nullable=True)
    receiver = Column(Integer, ForeignKey("source_receiver_flow.id"), nullable=True)
    redirect = Column(Integer, ForeignKey("source_redirect_flow.id"), nullable=True)
    sepa_credit_transfer = Column(
        Integer, ForeignKey("source_type_sepa_credit_transfer.id"), nullable=True
    )
    sepa_debit = Column(Integer, ForeignKey("source_type_sepa_debit.id"), nullable=True)
    sofort = Column(String, ForeignKey("source_type_sofort.bank_name"), nullable=True)
    source_order = Column(Integer, ForeignKey("source_order.id"), nullable=True)
    statement_descriptor = Column(
        String,
        comment="Extra information about a source. This will appear on your customer's statement every time you charge the source",
        nullable=True,
    )
    status = Column(
        String,
        comment="The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge",
    )
    three_d_secure = Column(
        Integer, ForeignKey("source_type_three_d_secure.id"), nullable=True
    )
    type = Column(
        String,
        comment="The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used",
    )
    usage = Column(
        String,
        comment="Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned",
        nullable=True,
    )
    wechat = Column(String, ForeignKey("source_type_wechat.prepay_id"), nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source(ach_credit_transfer={ach_credit_transfer!r}, ach_debit={ach_debit!r}, acss_debit={acss_debit!r}, alipay={alipay!r}, amount={amount!r}, au_becs_debit={au_becs_debit!r}, bancontact={bancontact!r}, card={card!r}, card_present={card_present!r}, client_secret={client_secret!r}, code_verification={code_verification!r}, created={created!r}, currency={currency!r}, customer={customer!r}, eps={eps!r}, flow={flow!r}, giropay={giropay!r}, id={id!r}, ideal={ideal!r}, klarna={klarna!r}, livemode={livemode!r}, metadata={metadata!r}, multibanco={multibanco!r}, object={object!r}, owner={owner!r}, p24={p24!r}, receiver={receiver!r}, redirect={redirect!r}, sepa_credit_transfer={sepa_credit_transfer!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, source_order={source_order!r}, statement_descriptor={statement_descriptor!r}, status={status!r}, three_d_secure={three_d_secure!r}, type={type!r}, usage={usage!r}, wechat={wechat!r})".format(
            ach_credit_transfer=self.ach_credit_transfer,
            ach_debit=self.ach_debit,
            acss_debit=self.acss_debit,
            alipay=self.alipay,
            amount=self.amount,
            au_becs_debit=self.au_becs_debit,
            bancontact=self.bancontact,
            card=self.card,
            card_present=self.card_present,
            client_secret=self.client_secret,
            code_verification=self.code_verification,
            created=self.created,
            currency=self.currency,
            customer=self.customer,
            eps=self.eps,
            flow=self.flow,
            giropay=self.giropay,
            id=self.id,
            ideal=self.ideal,
            klarna=self.klarna,
            livemode=self.livemode,
            metadata=self.metadata,
            multibanco=self.multibanco,
            object=self.object,
            owner=self.owner,
            p24=self.p24,
            receiver=self.receiver,
            redirect=self.redirect,
            sepa_credit_transfer=self.sepa_credit_transfer,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            source_order=self.source_order,
            statement_descriptor=self.statement_descriptor,
            status=self.status,
            three_d_secure=self.three_d_secure,
            type=self.type,
            usage=self.usage,
            wechat=self.wechat,
        )


__all__ = ["source"]
