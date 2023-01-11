from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class LegalEntityCompanyVerificationDocument(Base):
    __tablename__ = "legal_entity_company_verification_document"
    back = Column(
        File,
        ForeignKey("File"),
        comment="The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`",
        nullable=True,
    )
    details = Column(
        String,
        comment="A user-displayable string describing the verification state of this document",
        nullable=True,
    )
    details_code = Column(
        String,
        comment="One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document",
        nullable=True,
    )
    front = Column(
        File,
        ForeignKey("File"),
        comment="The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "LegalEntityCompanyVerificationDocument(back={back!r}, details={details!r}, details_code={details_code!r}, front={front!r}, id={id!r})".format(
            back=self.back,
            details=self.details,
            details_code=self.details_code,
            front=self.front,
            id=self.id,
        )


__all__ = ["legal_entity_company_verification_document"]
