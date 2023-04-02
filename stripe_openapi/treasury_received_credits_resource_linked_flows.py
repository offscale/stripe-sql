from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TreasuryReceivedCreditsResourceLinkedFlowsJson = Table(
    "treasury_received_credits_resource_linked_flowsjson",
    metadata,
    Column(
        "credit_reversal",
        String,
        comment="The CreditReversal created as a result of this ReceivedCredit being reversed",
        nullable=True,
    ),
    Column(
        "issuing_authorization",
        String,
        comment="Set if the ReceivedCredit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object",
        nullable=True,
    ),
    Column(
        "issuing_transaction",
        String,
        comment="Set if the ReceivedCredit is also viewable as an [Issuing transaction](https://stripe.com/docs/api#issuing_transactions) object",
        nullable=True,
    ),
    Column(
        "source_flow",
        String,
        comment="ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals",
        nullable=True,
    ),
    Column(
        "source_flow_details",
        TreasuryReceivedCreditsResourceSourceFlowsDetails,
        ForeignKey("TreasuryReceivedCreditsResourceSourceFlowsDetails"),
        comment="The expandable object of the source flow",
        nullable=True,
    ),
    Column(
        "source_flow_type",
        String,
        comment="The type of flow that originated the ReceivedCredit (for example, `outbound_payment`)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_credits_resource_linked_flows.json"]
