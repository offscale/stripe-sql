from sqlalchemy import Column, Integer, String


class Gelato_Document_Report(Base):
    """
    Result from a document check
    """

    __tablename__ = "gelato_document_report"
    address = Column(
        Address, comment="Address as it appears in the document", nullable=True
    )
    dob = Column(
        GelatoDataDocumentReportDateOfBirth,
        comment="Date of birth as it appears in the document",
        nullable=True,
    )
    error = Column(
        GelatoDocumentReportError,
        comment="Details on the verification error. Present when status is `unverified`",
        nullable=True,
    )
    expiration_date = Column(
        GelatoDataDocumentReportExpirationDate,
        comment="Expiration date of the document",
        nullable=True,
    )
    files = Column(
        ARRAY(String),
        comment="Array of [File](https://stripe.com/docs/api/files) ids containing images for this document",
        nullable=True,
    )
    first_name = Column(
        String, comment="First name as it appears in the document", nullable=True
    )
    issued_date = Column(
        GelatoDataDocumentReportIssuedDate,
        comment="Issued date of the document",
        nullable=True,
    )
    issuing_country = Column(
        String, comment="Issuing country of the document", nullable=True
    )
    last_name = Column(
        String, comment="Last name as it appears in the document", nullable=True
    )
    number = Column(String, comment="Document ID number", nullable=True)
    status = Column(String, comment="Status of this `document` check")
    type = Column(String, comment="Type of the document", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Gelato_Document_Report(address={address!r}, dob={dob!r}, error={error!r}, expiration_date={expiration_date!r}, files={files!r}, first_name={first_name!r}, issued_date={issued_date!r}, issuing_country={issuing_country!r}, last_name={last_name!r}, number={number!r}, status={status!r}, type={type!r}, id={id!r})".format(
            address=self.address,
            dob=self.dob,
            error=self.error,
            expiration_date=self.expiration_date,
            files=self.files,
            first_name=self.first_name,
            issued_date=self.issued_date,
            issuing_country=self.issuing_country,
            last_name=self.last_name,
            number=self.number,
            status=self.status,
            type=self.type,
            id=self.id,
        )


__all__ = ["gelato_document_report"]
