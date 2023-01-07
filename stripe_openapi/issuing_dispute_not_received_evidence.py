from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Not_Received_Evidence(Base):
    __tablename__ = "issuing_dispute_not_received_evidence"
    additional_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    expected_at = Column(
        Integer,
        comment="Date when the cardholder expected to receive the product",
        nullable=True,
    )
    explanation = Column(
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    )
    product_description = Column(
        String,
        comment="Description of the merchandise or service that was purchased",
        nullable=True,
    )
    product_type = Column(
        String,
        comment="Whether the product was a merchandise or service",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Not_Received_Evidence(additional_documentation={additional_documentation!r}, expected_at={expected_at!r}, explanation={explanation!r}, product_description={product_description!r}, product_type={product_type!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            expected_at=self.expected_at,
            explanation=self.explanation,
            product_description=self.product_description,
            product_type=self.product_type,
            id=self.id,
        )


__all__ = ["issuing_dispute_not_received_evidence"]
