from sqlalchemy import Column, Integer, String


class Refund_Next_Action(Base):
    __tablename__ = "refund_next_action"
    display_details = Column(
        RefundNextActionDisplayDetails,
        comment="Contains the refund details",
        nullable=True,
    )
    type = Column(String, comment="Type of the next action to perform")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Refund_Next_Action(display_details={display_details!r}, type={type!r}, id={id!r})".format(
            display_details=self.display_details, type=self.type, id=self.id
        )


__all__ = ["refund_next_action"]
