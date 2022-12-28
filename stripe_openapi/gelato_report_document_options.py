from sqlalchemy import Boolean, Column

class Gelato_Report_Document_Options(Base):
    __tablename__ = 'gelato_report_document_options'
    allowed_types = Column(ARRAY(String), comment='Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code', nullable=True)
    require_id_number = Column(Boolean, comment='Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document’s extracted name and date of birth', nullable=True, primary_key=True)
    require_live_capture = Column(Boolean, comment='Disable image uploads, identity document images have to be captured using the device’s camera', nullable=True)
    require_matching_selfie = Column(Boolean, comment='Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://stripe.com/docs/identity/selfie)', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Gelato_Report_Document_Options(allowed_types={allowed_types!r}, require_id_number={require_id_number!r}, require_live_capture={require_live_capture!r}, require_matching_selfie={require_matching_selfie!r})'.format(allowed_types=self.allowed_types, require_id_number=self.require_id_number, require_live_capture=self.require_live_capture, require_matching_selfie=self.require_matching_selfie)
__all__ = ['gelato_report_document_options']