from sqlalchemy import Column, ForeignKey

from stripe_openapi.gelato_report_id_number_options import GelatoReportIdNumberOptions

from . import Base


class GelatoVerificationReportOptions(Base):
    __tablename__ = "gelato_verification_report_options"
    document = Column(
        Boolean,
        ForeignKey("gelato_report_document_options.require_id_number"),
        nullable=True,
    )
    id_number = Column(
        GelatoReportIdNumberOptions,
        comment="[FK(GelatoReportIdNumberOptions)]",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoVerificationReportOptions(document={document!r}, id_number={id_number!r})".format(
            document=self.document, id_number=self.id_number
        )


__all__ = ["gelato_verification_report_options"]
