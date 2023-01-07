from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Duplicate_Evidence(Base):
    __tablename__ = "issuing_dispute_duplicate_evidence"
    additional_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    card_statement = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for",
        nullable=True,
    )
    cash_receipt = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash",
        nullable=True,
    )
    check_image = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product",
        nullable=True,
    )
    explanation = Column(
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    )
    original_transaction = Column(
        String,
        comment="Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Duplicate_Evidence(additional_documentation={additional_documentation!r}, card_statement={card_statement!r}, cash_receipt={cash_receipt!r}, check_image={check_image!r}, explanation={explanation!r}, original_transaction={original_transaction!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            card_statement=self.card_statement,
            cash_receipt=self.cash_receipt,
            check_image=self.check_image,
            explanation=self.explanation,
            original_transaction=self.original_transaction,
            id=self.id,
        )


__all__ = ["issuing_dispute_duplicate_evidence"]
