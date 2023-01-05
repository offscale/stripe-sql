from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Merchandise_Not_As_Described_Evidence(Base):
    __tablename__ = "issuing_dispute_merchandise_not_as_described_evidence"
    additional_documentation = Column(
        File,
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    explanation = Column(
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    )
    received_at = Column(
        Integer, comment="Date when the product was received", nullable=True
    )
    return_description = Column(
        String,
        comment="Description of the cardholder's attempt to return the product",
        nullable=True,
    )
    return_status = Column(
        String,
        comment="Result of cardholder's attempt to return the product",
        nullable=True,
    )
    returned_at = Column(
        Integer,
        comment="Date when the product was returned or attempted to be returned",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Merchandise_Not_As_Described_Evidence(additional_documentation={additional_documentation!r}, explanation={explanation!r}, received_at={received_at!r}, return_description={return_description!r}, return_status={return_status!r}, returned_at={returned_at!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            explanation=self.explanation,
            received_at=self.received_at,
            return_description=self.return_description,
            return_status=self.return_status,
            returned_at=self.returned_at,
            id=self.id,
        )


__all__ = ["issuing_dispute_merchandise_not_as_described_evidence"]
