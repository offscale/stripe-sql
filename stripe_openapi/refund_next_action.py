from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.refund_next_action_display_details import (
    RefundNextActionDisplayDetails,
)

from . import Base


class RefundNextAction(Base):
    __tablename__ = "refund_next_action"
    display_details = Column(
        RefundNextActionDisplayDetails,
        comment="[[FK(RefundNextActionDisplayDetails)]] Contains the refund details",
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
        return "RefundNextAction(display_details={display_details!r}, type={type!r}, id={id!r})".format(
            display_details=self.display_details, type=self.type, id=self.id
        )


__all__ = ["refund_next_action"]
