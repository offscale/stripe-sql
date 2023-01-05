from sqlalchemy import Column, Integer, String


class Account_Capability_Future_Requirements(Base):
    __tablename__ = "account_capability_future_requirements"
    alternatives = Column(
        list,
        comment="Fields that are due and can be satisfied by providing the corresponding alternative fields instead",
        nullable=True,
    )
    current_deadline = Column(
        Integer,
        comment="Date on which `future_requirements` merges with the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on the capability's enablement state prior to transitioning",
        nullable=True,
    )
    currently_due = Column(
        ARRAY(String),
        comment="Fields that need to be collected to keep the capability enabled. If not collected by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash",
    )
    disabled_reason = Column(
        String,
        comment="This is typed as a string for consistency with `requirements.disabled_reason`, but it safe to assume `future_requirements.disabled_reason` is empty because fields in `future_requirements` will never disable the account",
        nullable=True,
    )
    errors = Column(
        list,
        comment="Fields that are `currently_due` and need to be collected again because validation or verification failed",
    )
    eventually_due = Column(
        ARRAY(String),
        comment="Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well",
    )
    past_due = Column(
        ARRAY(String),
        comment="Fields that weren't collected by `requirements.current_deadline`. These fields need to be collected to enable the capability on the account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`",
    )
    pending_verification = Column(
        ARRAY(String),
        comment="Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Capability_Future_Requirements(alternatives={alternatives!r}, current_deadline={current_deadline!r}, currently_due={currently_due!r}, disabled_reason={disabled_reason!r}, errors={errors!r}, eventually_due={eventually_due!r}, past_due={past_due!r}, pending_verification={pending_verification!r}, id={id!r})".format(
            alternatives=self.alternatives,
            current_deadline=self.current_deadline,
            currently_due=self.currently_due,
            disabled_reason=self.disabled_reason,
            errors=self.errors,
            eventually_due=self.eventually_due,
            past_due=self.past_due,
            pending_verification=self.pending_verification,
            id=self.id,
        )


__all__ = ["account_capability_future_requirements"]
