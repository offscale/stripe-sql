from sqlalchemy import Column, Integer, String

class Source_Type_Card_Present(Base):
    __tablename__ = 'source_type_card_present'
    application_cryptogram = Column(String, nullable=True)
    application_preferred_name = Column(String, nullable=True)
    authorization_code = Column(String, nullable=True)
    authorization_response_code = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    country = Column(String, nullable=True)
    cvm_type = Column(String, nullable=True)
    data_type = Column(String, nullable=True)
    dedicated_file_name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    emv_auth_data = Column(String, nullable=True)
    evidence_customer_signature = Column(String, nullable=True)
    evidence_transaction_certificate = Column(String, nullable=True)
    exp_month = Column(Integer, nullable=True)
    exp_year = Column(Integer, nullable=True)
    fingerprint = Column(String, nullable=True)
    funding = Column(String, nullable=True)
    iin = Column(String, nullable=True)
    issuer = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    pos_device_id = Column(String, nullable=True)
    pos_entry_mode = Column(String, nullable=True)
    read_method = Column(String, nullable=True)
    reader = Column(String, nullable=True)
    terminal_verification_results = Column(String, nullable=True)
    transaction_status_information = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Card_Present(application_cryptogram={application_cryptogram!r}, application_preferred_name={application_preferred_name!r}, authorization_code={authorization_code!r}, authorization_response_code={authorization_response_code!r}, brand={brand!r}, country={country!r}, cvm_type={cvm_type!r}, data_type={data_type!r}, dedicated_file_name={dedicated_file_name!r}, description={description!r}, emv_auth_data={emv_auth_data!r}, evidence_customer_signature={evidence_customer_signature!r}, evidence_transaction_certificate={evidence_transaction_certificate!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, iin={iin!r}, issuer={issuer!r}, last4={last4!r}, pos_device_id={pos_device_id!r}, pos_entry_mode={pos_entry_mode!r}, read_method={read_method!r}, reader={reader!r}, terminal_verification_results={terminal_verification_results!r}, transaction_status_information={transaction_status_information!r}, id={id!r})'.format(application_cryptogram=self.application_cryptogram, application_preferred_name=self.application_preferred_name, authorization_code=self.authorization_code, authorization_response_code=self.authorization_response_code, brand=self.brand, country=self.country, cvm_type=self.cvm_type, data_type=self.data_type, dedicated_file_name=self.dedicated_file_name, description=self.description, emv_auth_data=self.emv_auth_data, evidence_customer_signature=self.evidence_customer_signature, evidence_transaction_certificate=self.evidence_transaction_certificate, exp_month=self.exp_month, exp_year=self.exp_year, fingerprint=self.fingerprint, funding=self.funding, iin=self.iin, issuer=self.issuer, last4=self.last4, pos_device_id=self.pos_device_id, pos_entry_mode=self.pos_entry_mode, read_method=self.read_method, reader=self.reader, terminal_verification_results=self.terminal_verification_results, transaction_status_information=self.transaction_status_information, id=self.id)
__all__ = ['source_type_card_present']