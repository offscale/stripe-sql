from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PortalFlowsAfterCompletionHostedConfirmation(Base):
    __tablename__ = "portal_flows_after_completion_hosted_confirmation"
    custom_message = Column(
        String,
        comment="A custom message to display to the customer after the flow is completed",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalFlowsAfterCompletionHostedConfirmation(custom_message={custom_message!r}, id={id!r})".format(
            custom_message=self.custom_message, id=self.id
        )


__all__ = ["portal_flows_after_completion_hosted_confirmation"]
