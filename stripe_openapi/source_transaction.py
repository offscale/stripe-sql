from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from . import Base


class SourceTransaction(Base):
    """
    Some payment methods have no required amount that a customer must send.

    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.

    """

    __tablename__ = "source_transaction"
    ach_credit_transfer = Column(
        Integer,
        ForeignKey("source_transaction_ach_credit_transfer_data.id"),
        nullable=True,
    )
    amount = Column(
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount your customer has pushed to the receiver",
    )
    chf_credit_transfer = Column(
        String,
        ForeignKey("source_transaction_chf_credit_transfer_data.sender_name"),
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    gbp_credit_transfer = Column(
        String,
        ForeignKey("source_transaction_gbp_credit_transfer_data.sender_name"),
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    paper_check = Column(
        Integer, ForeignKey("source_transaction_paper_check_data.id"), nullable=True
    )
    sepa_credit_transfer = Column(
        String,
        ForeignKey("source_transaction_sepa_credit_transfer_data.sender_name"),
        nullable=True,
    )
    source = Column(
        String, comment="The ID of the source this transaction is attached to"
    )
    status = Column(
        String,
        comment="The status of the transaction, one of `succeeded`, `pending`, or `failed`",
    )
    type = Column(String, comment="The type of source this transaction is attached to")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTransaction(ach_credit_transfer={ach_credit_transfer!r}, amount={amount!r}, chf_credit_transfer={chf_credit_transfer!r}, created={created!r}, currency={currency!r}, gbp_credit_transfer={gbp_credit_transfer!r}, id={id!r}, livemode={livemode!r}, object={object!r}, paper_check={paper_check!r}, sepa_credit_transfer={sepa_credit_transfer!r}, source={source!r}, status={status!r}, type={type!r})".format(
            ach_credit_transfer=self.ach_credit_transfer,
            amount=self.amount,
            chf_credit_transfer=self.chf_credit_transfer,
            created=self.created,
            currency=self.currency,
            gbp_credit_transfer=self.gbp_credit_transfer,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            paper_check=self.paper_check,
            sepa_credit_transfer=self.sepa_credit_transfer,
            source=self.source,
            status=self.status,
            type=self.type,
        )


__all__ = ["source_transaction"]
