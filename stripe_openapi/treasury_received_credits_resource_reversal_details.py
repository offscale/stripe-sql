from sqlalchemy import Column, Identity, Integer, String

from . import Base


class TreasuryReceivedCreditsResourceReversalDetails(Base):
    __tablename__ = "treasury_received_credits_resource_reversal_details"
    deadline = Column(
        Integer,
        comment="Time before which a ReceivedCredit can be reversed",
        nullable=True,
    )
    restricted_reason = Column(
        String, comment="Set if a ReceivedCredit cannot be reversed", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryReceivedCreditsResourceReversalDetails(deadline={deadline!r}, restricted_reason={restricted_reason!r}, id={id!r})".format(
            deadline=self.deadline, restricted_reason=self.restricted_reason, id=self.id
        )


__all__ = ["treasury_received_credits_resource_reversal_details"]
