from sqlalchemy import ARRAY, Boolean, Column, String, Table

from . import metadata

GelatoReportDocumentOptions.Json = Table(
    "gelato_report_document_options.json",
    metadata,
    Column(
        "allowed_types",
        ARRAY(String),
        comment="Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code",
        nullable=True,
    ),
    Column(
        "require_id_number",
        Boolean,
        comment="Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document’s extracted name and date of birth",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "require_live_capture",
        Boolean,
        comment="Disable image uploads, identity document images have to be captured using the device’s camera",
        nullable=True,
    ),
    Column(
        "require_matching_selfie",
        Boolean,
        comment="Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://stripe.com/docs/identity/selfie)",
        nullable=True,
    ),
)
__all__ = ["gelato_report_document_options.json"]
