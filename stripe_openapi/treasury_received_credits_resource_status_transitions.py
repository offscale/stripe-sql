from sqlalchemy import Column, Identity, Integer

from . import Base


class TreasuryReceivedCreditsResourceStatusTransitions(Base):
    __tablename__ = "treasury_received_credits_resource_status_transitions"
    posted_at = Column(
        Integer,
        comment="Timestamp describing when the CreditReversal changed status to `posted`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryReceivedCreditsResourceStatusTransitions(posted_at={posted_at!r}, id={id!r})".format(
            posted_at=self.posted_at, id=self.id
        )


__all__ = ["treasury_received_credits_resource_status_transitions"]
