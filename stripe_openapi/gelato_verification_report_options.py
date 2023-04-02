from sqlalchemy import Column, ForeignKey, Table

from . import metadata

GelatoVerificationReportOptionsJson = Table(
    "gelato_verification_report_optionsjson",
    metadata,
    Column(
        "document",
        GelatoReportDocumentOptions,
        ForeignKey("GelatoReportDocumentOptions"),
        nullable=True,
    ),
    Column(
        "id_number",
        GelatoReportIdNumberOptions,
        comment="[FK(GelatoReportIdNumberOptions)]",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["gelato_verification_report_options.json"]
