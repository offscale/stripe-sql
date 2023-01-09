from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.portal_flows_after_completion_hosted_confirmation import (
    PortalFlowsAfterCompletionHostedConfirmation,
)
from stripe_openapi.portal_flows_after_completion_redirect import (
    PortalFlowsAfterCompletionRedirect,
)

from . import Base


class PortalFlowsFlowAfterCompletion(Base):
    __tablename__ = "portal_flows_flow_after_completion"
    hosted_confirmation = Column(
        PortalFlowsAfterCompletionHostedConfirmation,
        comment="[[FK(PortalFlowsAfterCompletionHostedConfirmation)]] Configuration when `after_completion.type=hosted_confirmation`",
        nullable=True,
    )
    redirect = Column(
        PortalFlowsAfterCompletionRedirect,
        comment="[[FK(PortalFlowsAfterCompletionRedirect)]] Configuration when `after_completion.type=redirect`",
        nullable=True,
    )
    type = Column(
        String, comment="The specified type of behavior after the flow is completed"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalFlowsFlowAfterCompletion(hosted_confirmation={hosted_confirmation!r}, redirect={redirect!r}, type={type!r}, id={id!r})".format(
            hosted_confirmation=self.hosted_confirmation,
            redirect=self.redirect,
            type=self.type,
            id=self.id,
        )


__all__ = ["portal_flows_flow_after_completion"]
