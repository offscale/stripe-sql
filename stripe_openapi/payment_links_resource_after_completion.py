from sqlalchemy import Column, Integer, String

class Payment_Links_Resource_After_Completion(Base):
    __tablename__ = 'payment_links_resource_after_completion'
    hosted_confirmation = Column(PaymentLinksResourceCompletionBehaviorConfirmationPage, nullable=True)
    redirect = Column(PaymentLinksResourceCompletionBehaviorRedirect, nullable=True)
    type = Column(String, comment='The specified behavior after the purchase is complete')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Links_Resource_After_Completion(hosted_confirmation={hosted_confirmation!r}, redirect={redirect!r}, type={type!r}, id={id!r})'.format(hosted_confirmation=self.hosted_confirmation, redirect=self.redirect, type=self.type, id=self.id)
__all__ = ['payment_links_resource_after_completion']