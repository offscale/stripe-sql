from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class TreasuryReceivedCreditsResourceLinkedFlows(Base):
    __tablename__ = "treasury_received_credits_resource_linked_flows"
    credit_reversal = Column(
        String,
        comment="The CreditReversal created as a result of this ReceivedCredit being reversed",
        nullable=True,
    )
    issuing_authorization = Column(
        String,
        comment="Set if the ReceivedCredit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object",
        nullable=True,
    )
    issuing_transaction = Column(
        String,
        comment="Set if the ReceivedCredit is also viewable as an [Issuing transaction](https://stripe.com/docs/api#issuing_transactions) object",
        nullable=True,
    )
    source_flow = Column(
        String,
        comment="ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals",
        nullable=True,
    )
    source_flow_details = Column(
        Integer,
        ForeignKey("treasury_received_credits_resource_source_flows_details.id"),
        comment="The expandable object of the source flow",
        nullable=True,
    )
    source_flow_type = Column(
        String,
        comment="The type of flow that originated the ReceivedCredit (for example, `outbound_payment`)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryReceivedCreditsResourceLinkedFlows(credit_reversal={credit_reversal!r}, issuing_authorization={issuing_authorization!r}, issuing_transaction={issuing_transaction!r}, source_flow={source_flow!r}, source_flow_details={source_flow_details!r}, source_flow_type={source_flow_type!r}, id={id!r})".format(
            credit_reversal=self.credit_reversal,
            issuing_authorization=self.issuing_authorization,
            issuing_transaction=self.issuing_transaction,
            source_flow=self.source_flow,
            source_flow_details=self.source_flow_details,
            source_flow_type=self.source_flow_type,
            id=self.id,
        )


__all__ = ["treasury_received_credits_resource_linked_flows"]
