from sqlalchemy import Column, Identity, Integer, String

from . import Base


class IssuingDisputeServiceNotAsDescribedEvidence(Base):
    __tablename__ = "issuing_dispute_service_not_as_described_evidence"
    additional_documentation = Column(
        File,
        comment="[[FK(File)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    canceled_at = Column(Integer, comment="Date when order was canceled", nullable=True)
    cancellation_reason = Column(
        String, comment="Reason for canceling the order", nullable=True
    )
    explanation = Column(
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    )
    received_at = Column(
        Integer, comment="Date when the product was received", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingDisputeServiceNotAsDescribedEvidence(additional_documentation={additional_documentation!r}, canceled_at={canceled_at!r}, cancellation_reason={cancellation_reason!r}, explanation={explanation!r}, received_at={received_at!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            canceled_at=self.canceled_at,
            cancellation_reason=self.cancellation_reason,
            explanation=self.explanation,
            received_at=self.received_at,
            id=self.id,
        )


__all__ = ["issuing_dispute_service_not_as_described_evidence"]
