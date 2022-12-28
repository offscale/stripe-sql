from sqlalchemy import Boolean, Column, Integer, String

class Capability(Base):
    """
        This is an object representing a capability for a Stripe account.
    
        Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities).
    
        """
    __tablename__ = 'capability'
    account = Column(Account, comment='The account for which the capability enables functionality')
    future_requirements = Column(AccountCapabilityFutureRequirements, nullable=True)
    id = Column(String, comment='The identifier for the capability', primary_key=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    requested = Column(Boolean, comment='Whether the capability has been requested')
    requested_at = Column(Integer, comment='Time at which the capability was requested. Measured in seconds since the Unix epoch', nullable=True)
    requirements = Column(AccountCapabilityRequirements, nullable=True)
    status = Column(String, comment='The status of the capability. Can be `active`, `inactive`, `pending`, or `unrequested`')

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Capability(account={account!r}, future_requirements={future_requirements!r}, id={id!r}, object={object!r}, requested={requested!r}, requested_at={requested_at!r}, requirements={requirements!r}, status={status!r})'.format(account=self.account, future_requirements=self.future_requirements, id=self.id, object=self.object, requested=self.requested, requested_at=self.requested_at, requirements=self.requirements, status=self.status)
__all__ = ['capability']