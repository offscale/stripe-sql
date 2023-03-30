from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

IssuingDisputeEvidence.Json = Table(
    "issuing_dispute_evidence.json",
    metadata,
    Column(
        "canceled",
        IssuingDisputeCanceledEvidence,
        ForeignKey("IssuingDisputeCanceledEvidence"),
        nullable=True,
    ),
    Column(
        "duplicate",
        IssuingDisputeDuplicateEvidence,
        ForeignKey("IssuingDisputeDuplicateEvidence"),
        nullable=True,
    ),
    Column(
        "fraudulent",
        IssuingDisputeFraudulentEvidence,
        ForeignKey("IssuingDisputeFraudulentEvidence"),
        nullable=True,
    ),
    Column(
        "merchandise_not_as_described",
        IssuingDisputeMerchandiseNotAsDescribedEvidence,
        ForeignKey("IssuingDisputeMerchandiseNotAsDescribedEvidence"),
        nullable=True,
    ),
    Column(
        "not_received",
        IssuingDisputeNotReceivedEvidence,
        ForeignKey("IssuingDisputeNotReceivedEvidence"),
        nullable=True,
    ),
    Column(
        "other",
        IssuingDisputeOtherEvidence,
        ForeignKey("IssuingDisputeOtherEvidence"),
        nullable=True,
    ),
    Column(
        "reason",
        String,
        comment="The reason for filing the dispute. Its value will match the field containing the evidence",
    ),
    Column(
        "service_not_as_described",
        IssuingDisputeServiceNotAsDescribedEvidence,
        ForeignKey("IssuingDisputeServiceNotAsDescribedEvidence"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_evidence.json"]
