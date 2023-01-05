from sqlalchemy import Column, Integer, String


class Setup_Intent_Next_Action_Verify_With_Microdeposits(Base):
    __tablename__ = "setup_intent_next_action_verify_with_microdeposits"
    arrival_date = Column(
        Integer, comment="The timestamp when the microdeposits are expected to land"
    )
    hosted_verification_url = Column(
        String,
        comment="The URL for the hosted verification page, which allows customers to verify their bank account",
    )
    microdeposit_type = Column(
        String,
        comment="The type of the microdeposit sent to the customer. Used to distinguish between different verification methods",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Intent_Next_Action_Verify_With_Microdeposits(arrival_date={arrival_date!r}, hosted_verification_url={hosted_verification_url!r}, microdeposit_type={microdeposit_type!r}, id={id!r})".format(
            arrival_date=self.arrival_date,
            hosted_verification_url=self.hosted_verification_url,
            microdeposit_type=self.microdeposit_type,
            id=self.id,
        )


__all__ = ["setup_intent_next_action_verify_with_microdeposits"]
