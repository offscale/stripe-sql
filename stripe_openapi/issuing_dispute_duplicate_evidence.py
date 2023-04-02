from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeDuplicateEvidenceJson = Table(
    "issuing_dispute_duplicate_evidencejson",
    metadata,
    Column(
        "additional_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    ),
    Column(
        "card_statement",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for",
        nullable=True,
    ),
    Column(
        "cash_receipt",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash",
        nullable=True,
    ),
    Column(
        "check_image",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product",
        nullable=True,
    ),
    Column(
        "explanation",
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    ),
    Column(
        "original_transaction",
        String,
        comment="Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_duplicate_evidence.json"]
