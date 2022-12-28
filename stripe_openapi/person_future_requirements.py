from sqlalchemy import Column, Integer

class Person_Future_Requirements(Base):
    __tablename__ = 'person_future_requirements'
    alternatives = Column(list, comment='Fields that are due and can be satisfied by providing the corresponding alternative fields instead', nullable=True)
    currently_due = Column(ARRAY(String), comment="Fields that need to be collected to keep the person's account enabled. If not collected by the account's `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash, and may immediately become `past_due`, but the account may also be given a grace period depending on the account's enablement state prior to transition")
    errors = Column(list, comment='Fields that are `currently_due` and need to be collected again because validation or verification failed')
    eventually_due = Column(ARRAY(String), comment="Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and the account's `future_requirements[current_deadline]` becomes set")
    past_due = Column(ARRAY(String), comment="Fields that weren't collected by the account's `requirements.current_deadline`. These fields need to be collected to enable the person's account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`")
    pending_verification = Column(ARRAY(String), comment='Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Person_Future_Requirements(alternatives={alternatives!r}, currently_due={currently_due!r}, errors={errors!r}, eventually_due={eventually_due!r}, past_due={past_due!r}, pending_verification={pending_verification!r}, id={id!r})'.format(alternatives=self.alternatives, currently_due=self.currently_due, errors=self.errors, eventually_due=self.eventually_due, past_due=self.past_due, pending_verification=self.pending_verification, id=self.id)
__all__ = ['person_future_requirements']