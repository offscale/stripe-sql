from sqlalchemy import Column, Identity, Integer, String

from . import Base


class IssuingDisputeOtherEvidence(Base):
    __tablename__ = "issuing_dispute_other_evidence"
    additional_documentation = Column(
        File,
        comment="[[FK(File)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
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
        return "IssuingDisputeOtherEvidence(additional_documentation={additional_documentation!r}, explanation={explanation!r}, product_description={product_description!r}, product_type={product_type!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            explanation=self.explanation,
            product_description=self.product_description,
            product_type=self.product_type,
            id=self.id,
        )


__all__ = ["issuing_dispute_other_evidence"]
