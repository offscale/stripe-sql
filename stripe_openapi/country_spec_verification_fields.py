from sqlalchemy import Column, Integer

class Country_Spec_Verification_Fields(Base):
    __tablename__ = 'country_spec_verification_fields'
    company = Column(CountrySpecVerificationFieldDetails)
    individual = Column(CountrySpecVerificationFieldDetails)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Country_Spec_Verification_Fields(company={company!r}, individual={individual!r}, id={id!r})'.format(company=self.company, individual=self.individual, id=self.id)
__all__ = ['country_spec_verification_fields']