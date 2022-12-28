from sqlalchemy import Column, Integer, String

class Legal_Entity_Person_Verification(Base):
    __tablename__ = 'legal_entity_person_verification'
    additional_document = Column(LegalEntityPersonVerificationDocument, comment='A document showing address, either a passport, local ID card, or utility bill from a well-known utility company', nullable=True)
    details = Column(String, comment='A user-displayable string describing the verification state for the person. For example, this may say "Provided identity information could not be verified"', nullable=True)
    details_code = Column(String, comment='One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person', nullable=True)
    document = Column(LegalEntityPersonVerificationDocument, nullable=True)
    status = Column(String, comment='The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Legal_Entity_Person_Verification(additional_document={additional_document!r}, details={details!r}, details_code={details_code!r}, document={document!r}, status={status!r}, id={id!r})'.format(additional_document=self.additional_document, details=self.details, details_code=self.details_code, document=self.document, status=self.status, id=self.id)
__all__ = ['legal_entity_person_verification']