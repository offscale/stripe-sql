from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.payout import Payout

from . import metadata

TreasuryReceivedCreditsResourceSourceFlowsDetailsJson = Table(
    "treasury_received_credits_resource_source_flows_detailsjson",
    metadata,
    Column(
        "credit_reversal",
        Treasury__CreditReversal,
        ForeignKey("Treasury__CreditReversal"),
        nullable=True,
    ),
    Column(
        "outbound_payment",
        Treasury__OutboundPayment,
        ForeignKey("Treasury__OutboundPayment"),
        nullable=True,
    ),
    Column("payout", Payout, ForeignKey("Payout"), nullable=True),
    Column(
        "type",
        String,
        comment="The type of the source flow that originated the ReceivedCredit",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_credits_resource_source_flows_details.json"]
