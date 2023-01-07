from sqlalchemy import Boolean, Column, Integer, String


class Issuing_Dispute_Canceled_Evidence(Base):
    __tablename__ = "issuing_dispute_canceled_evidence"
    additional_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    canceled_at = Column(Integer, comment="Date when order was canceled", nullable=True)
    cancellation_policy_provided = Column(
        Boolean,
        comment="Whether the cardholder was provided with a cancellation policy",
        nullable=True,
    )
    cancellation_reason = Column(
        String, comment="Reason for canceling the order", nullable=True
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
        return "Issuing_Dispute_Canceled_Evidence(additional_documentation={additional_documentation!r}, canceled_at={canceled_at!r}, cancellation_policy_provided={cancellation_policy_provided!r}, cancellation_reason={cancellation_reason!r}, expected_at={expected_at!r}, explanation={explanation!r}, product_description={product_description!r}, product_type={product_type!r}, return_status={return_status!r}, returned_at={returned_at!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            canceled_at=self.canceled_at,
            cancellation_policy_provided=self.cancellation_policy_provided,
            cancellation_reason=self.cancellation_reason,
            expected_at=self.expected_at,
            explanation=self.explanation,
            product_description=self.product_description,
            product_type=self.product_type,
            return_status=self.return_status,
            returned_at=self.returned_at,
            id=self.id,
        )


__all__ = ["issuing_dispute_canceled_evidence"]
