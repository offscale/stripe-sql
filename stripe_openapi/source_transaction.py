from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from . import metadata

SourceTransactionJson = Table(
    "source_transactionjson",
    metadata,
    Column(
        "ach_credit_transfer",
        SourceTransactionAchCreditTransferData,
        ForeignKey("SourceTransactionAchCreditTransferData"),
        nullable=True,
    ),
    Column(
        "amount",
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount your customer has pushed to the receiver",
    ),
    Column(
        "chf_credit_transfer",
        SourceTransactionChfCreditTransferData,
        ForeignKey("SourceTransactionChfCreditTransferData"),
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
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "gbp_credit_transfer",
        SourceTransactionGbpCreditTransferData,
        ForeignKey("SourceTransactionGbpCreditTransferData"),
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "paper_check",
        SourceTransactionPaperCheckData,
        ForeignKey("SourceTransactionPaperCheckData"),
        nullable=True,
    ),
    Column(
        "sepa_credit_transfer",
        SourceTransactionSepaCreditTransferData,
        ForeignKey("SourceTransactionSepaCreditTransferData"),
        nullable=True,
    ),
    Column(
        "source", String, comment="The ID of the source this transaction is attached to"
    ),
    Column(
        "status",
        String,
        comment="The status of the transaction, one of `succeeded`, `pending`, or `failed`",
    ),
    Column(
        "type", String, comment="The type of source this transaction is attached to"
    ),
)
__all__ = ["source_transaction.json"]
