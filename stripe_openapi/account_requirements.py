from sqlalchemy import Column, Integer, String

class Account_Requirements(Base):
    __tablename__ = 'account_requirements'
    alternatives = Column(list, comment='Fields that are due and can be satisfied by providing the corresponding alternative fields instead', nullable=True)
    current_deadline = Column(Integer, comment='Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected', nullable=True)
    currently_due = Column(ARRAY(String), comment='Fields that need to be collected to keep the account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled', nullable=True)
    disabled_reason = Column(String, comment='If the account is disabled, this string describes why. Can be `requirements.past_due`, `requirements.pending_verification`, `listed`, `platform_paused`, `rejected.fraud`, `rejected.listed`, `rejected.terms_of_service`, `rejected.other`, `under_review`, or `other`', nullable=True)
    errors = Column(list, comment='Fields that are `currently_due` and need to be collected again because validation or verification failed', nullable=True)
    eventually_due = Column(ARRAY(String), comment='Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set', nullable=True)
    past_due = Column(ARRAY(String), comment="Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the account", nullable=True)
    pending_verification = Column(ARRAY(String), comment='Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Requirements(alternatives={alternatives!r}, current_deadline={current_deadline!r}, currently_due={currently_due!r}, disabled_reason={disabled_reason!r}, errors={errors!r}, eventually_due={eventually_due!r}, past_due={past_due!r}, pending_verification={pending_verification!r}, id={id!r})'.format(alternatives=self.alternatives, current_deadline=self.current_deadline, currently_due=self.currently_due, disabled_reason=self.disabled_reason, errors=self.errors, eventually_due=self.eventually_due, past_due=self.past_due, pending_verification=self.pending_verification, id=self.id)
__all__ = ['account_requirements']