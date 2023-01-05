from sqlalchemy import Column, Integer, String


class Treasury_Received_Debits_Resource_Reversal_Details(Base):
    __tablename__ = "treasury_received_debits_resource_reversal_details"
    deadline = Column(
        Integer,
        comment="Time before which a ReceivedDebit can be reversed",
        nullable=True,
    )
    restricted_reason = Column(
        String, comment="Set if a ReceivedDebit can't be reversed", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Received_Debits_Resource_Reversal_Details(deadline={deadline!r}, restricted_reason={restricted_reason!r}, id={id!r})".format(
            deadline=self.deadline, restricted_reason=self.restricted_reason, id=self.id
        )


__all__ = ["treasury_received_debits_resource_reversal_details"]
