from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from . import metadata

SourceJson = Table(
    "sourcejson",
    metadata,
    Column(
        "ach_credit_transfer",
        SourceTypeAchCreditTransfer,
        ForeignKey("SourceTypeAchCreditTransfer"),
        nullable=True,
    ),
    Column(
        "ach_debit", SourceTypeAchDebit, ForeignKey("SourceTypeAchDebit"), nullable=True
    ),
    Column(
        "acss_debit",
        SourceTypeAcssDebit,
        ForeignKey("SourceTypeAcssDebit"),
        nullable=True,
    ),
    Column("alipay", SourceTypeAlipay, ForeignKey("SourceTypeAlipay"), nullable=True),
    Column(
        "amount",
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources",
        nullable=True,
    ),
    Column(
        "au_becs_debit",
        SourceTypeAuBecsDebit,
        ForeignKey("SourceTypeAuBecsDebit"),
        nullable=True,
    ),
    Column(
        "bancontact",
        SourceTypeBancontact,
        ForeignKey("SourceTypeBancontact"),
        nullable=True,
    ),
    Column("card", SourceTypeCard, ForeignKey("SourceTypeCard"), nullable=True),
    Column(
        "card_present",
        SourceTypeCardPresent,
        ForeignKey("SourceTypeCardPresent"),
        nullable=True,
    ),
    Column(
        "client_secret",
        String,
        comment="The client secret of the source. Used for client-side retrieval using a publishable key",
    ),
    Column(
        "code_verification",
        SourceCodeVerificationFlow,
        ForeignKey("SourceCodeVerificationFlow"),
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources",
        nullable=True,
    ),
    Column(
        "customer",
        String,
        comment="The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer",
        nullable=True,
    ),
    Column("eps", SourceTypeEps, ForeignKey("SourceTypeEps"), nullable=True),
    Column(
        "flow",
        String,
        comment="The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`",
    ),
    Column(
        "giropay", SourceTypeGiropay, ForeignKey("SourceTypeGiropay"), nullable=True
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("ideal", SourceTypeIdeal, ForeignKey("SourceTypeIdeal"), nullable=True),
    Column("klarna", SourceTypeKlarna, ForeignKey("SourceTypeKlarna"), nullable=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "multibanco",
        SourceTypeMultibanco,
        ForeignKey("SourceTypeMultibanco"),
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "owner",
        SourceOwner,
        ForeignKey("SourceOwner"),
        comment="Information about the owner of the payment instrument that may be used or required by particular source types",
        nullable=True,
    ),
    Column("p24", SourceTypeP24, ForeignKey("SourceTypeP24"), nullable=True),
    Column(
        "receiver", SourceReceiverFlow, ForeignKey("SourceReceiverFlow"), nullable=True
    ),
    Column(
        "redirect", SourceRedirectFlow, ForeignKey("SourceRedirectFlow"), nullable=True
    ),
    Column(
        "sepa_credit_transfer",
        SourceTypeSepaCreditTransfer,
        ForeignKey("SourceTypeSepaCreditTransfer"),
        nullable=True,
    ),
    Column(
        "sepa_debit",
        SourceTypeSepaDebit,
        ForeignKey("SourceTypeSepaDebit"),
        nullable=True,
    ),
    Column("sofort", SourceTypeSofort, ForeignKey("SourceTypeSofort"), nullable=True),
    Column("source_order", SourceOrder, ForeignKey("SourceOrder"), nullable=True),
    Column(
        "statement_descriptor",
        String,
        comment="Extra information about a source. This will appear on your customer's statement every time you charge the source",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge",
    ),
    Column(
        "three_d_secure",
        SourceTypeThreeDSecure,
        ForeignKey("SourceTypeThreeDSecure"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used",
    ),
    Column(
        "usage",
        String,
        comment="Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned",
        nullable=True,
    ),
    Column("wechat", SourceTypeWechat, ForeignKey("SourceTypeWechat"), nullable=True),
)
__all__ = ["source.json"]
