from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

DisputeEvidenceDetailsJson = Table(
    "dispute_evidence_detailsjson",
    metadata,
    Column(
        "due_by",
        Integer,
        comment="Date by which evidence must be submitted in order to successfully challenge dispute. Will be 0 if the customer's bank or credit card company doesn't allow a response for this particular dispute",
        nullable=True,
    ),
    Column(
        "has_evidence",
        Boolean,
        comment="Whether evidence has been staged for this dispute",
    ),
    Column(
        "past_due",
        Boolean,
        comment="Whether the last evidence submission was submitted past the due date. Defaults to `false` if no evidence submissions have occurred. If `true`, then delivery of the latest evidence is *not* guaranteed",
    ),
    Column(
        "submission_count",
        Integer,
        comment="The number of times evidence has been submitted. Typically, you may only submit evidence once",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["dispute_evidence_details.json"]
