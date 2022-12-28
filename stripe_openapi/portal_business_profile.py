from sqlalchemy import Column, Integer, String

class Portal_Business_Profile(Base):
    __tablename__ = 'portal_business_profile'
    headline = Column(String, comment='The messaging shown to customers in the portal', nullable=True)
    privacy_policy_url = Column(String, comment='A link to the business’s publicly available privacy policy', nullable=True)
    terms_of_service_url = Column(String, comment='A link to the business’s publicly available terms of service', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Business_Profile(headline={headline!r}, privacy_policy_url={privacy_policy_url!r}, terms_of_service_url={terms_of_service_url!r}, id={id!r})'.format(headline=self.headline, privacy_policy_url=self.privacy_policy_url, terms_of_service_url=self.terms_of_service_url, id=self.id)
__all__ = ['portal_business_profile']