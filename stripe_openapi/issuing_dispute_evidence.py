from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class IssuingDisputeEvidence(Base):
    __tablename__ = "issuing_dispute_evidence"
    canceled = Column(
        Integer, ForeignKey("issuing_dispute_canceled_evidence.id"), nullable=True
    )
    duplicate = Column(
        Integer, ForeignKey("issuing_dispute_duplicate_evidence.id"), nullable=True
    )
    fraudulent = Column(
        Integer, ForeignKey("issuing_dispute_fraudulent_evidence.id"), nullable=True
    )
    merchandise_not_as_described = Column(
        Integer,
        ForeignKey("issuing_dispute_merchandise_not_as_described_evidence.id"),
        nullable=True,
    )
    not_received = Column(
        Integer, ForeignKey("issuing_dispute_not_received_evidence.id"), nullable=True
    )
    other = Column(
        Integer, ForeignKey("issuing_dispute_other_evidence.id"), nullable=True
    )
    reason = Column(
        String,
        comment="The reason for filing the dispute. Its value will match the field containing the evidence",
    )
    service_not_as_described = Column(
        Integer,
        ForeignKey("issuing_dispute_service_not_as_described_evidence.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingDisputeEvidence(canceled={canceled!r}, duplicate={duplicate!r}, fraudulent={fraudulent!r}, merchandise_not_as_described={merchandise_not_as_described!r}, not_received={not_received!r}, other={other!r}, reason={reason!r}, service_not_as_described={service_not_as_described!r}, id={id!r})".format(
            canceled=self.canceled,
            duplicate=self.duplicate,
            fraudulent=self.fraudulent,
            merchandise_not_as_described=self.merchandise_not_as_described,
            not_received=self.not_received,
            other=self.other,
            reason=self.reason,
            service_not_as_described=self.service_not_as_described,
            id=self.id,
        )


__all__ = ["issuing_dispute_evidence"]
