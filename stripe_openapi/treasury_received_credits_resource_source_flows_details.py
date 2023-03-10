from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from stripe_openapi.treasury__credit_reversal import Treasury__CreditReversal
from stripe_openapi.treasury__outbound_payment import Treasury__OutboundPayment

from . import Base


class TreasuryReceivedCreditsResourceSourceFlowsDetails(Base):
    __tablename__ = "treasury_received_credits_resource_source_flows_details"
    credit_reversal = Column(
        Treasury__CreditReversal, ForeignKey("Treasury__CreditReversal"), nullable=True
    )
    outbound_payment = Column(
        Treasury__OutboundPayment,
        ForeignKey("Treasury__OutboundPayment"),
        nullable=True,
    )
    payout = Column(Payout, ForeignKey("Payout"), nullable=True)
    type = Column(
        String, comment="The type of the source flow that originated the ReceivedCredit"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryReceivedCreditsResourceSourceFlowsDetails(credit_reversal={credit_reversal!r}, outbound_payment={outbound_payment!r}, payout={payout!r}, type={type!r}, id={id!r})".format(
            credit_reversal=self.credit_reversal,
            outbound_payment=self.outbound_payment,
            payout=self.payout,
            type=self.type,
            id=self.id,
        )


__all__ = ["treasury_received_credits_resource_source_flows_details"]
