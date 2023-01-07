from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Evidence(Base):
    __tablename__ = "issuing_dispute_evidence"
    canceled = Column(
        issuing_dispute_canceled_evidence,
        ForeignKey("issuing_dispute_canceled_evidence"),
        nullable=True,
    )
    duplicate = Column(
        issuing_dispute_duplicate_evidence,
        ForeignKey("issuing_dispute_duplicate_evidence"),
        nullable=True,
    )
    fraudulent = Column(
        issuing_dispute_fraudulent_evidence,
        ForeignKey("issuing_dispute_fraudulent_evidence"),
        nullable=True,
    )
    merchandise_not_as_described = Column(
        issuing_dispute_merchandise_not_as_described_evidence,
        ForeignKey("issuing_dispute_merchandise_not_as_described_evidence"),
        nullable=True,
    )
    not_received = Column(
        issuing_dispute_not_received_evidence,
        ForeignKey("issuing_dispute_not_received_evidence"),
        nullable=True,
    )
    other = Column(
        issuing_dispute_other_evidence,
        ForeignKey("issuing_dispute_other_evidence"),
        nullable=True,
    )
    reason = Column(
        String,
        comment="The reason for filing the dispute. Its value will match the field containing the evidence",
    )
    service_not_as_described = Column(
        issuing_dispute_service_not_as_described_evidence,
        ForeignKey("issuing_dispute_service_not_as_described_evidence"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Evidence(canceled={canceled!r}, duplicate={duplicate!r}, fraudulent={fraudulent!r}, merchandise_not_as_described={merchandise_not_as_described!r}, not_received={not_received!r}, other={other!r}, reason={reason!r}, service_not_as_described={service_not_as_described!r}, id={id!r})".format(
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
