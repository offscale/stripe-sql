from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.issuing__authorization import Issuing__Authorization

from . import metadata

TreasuryTransactionsResourceFlowDetailsJson = Table(
    "treasury_transactions_resource_flow_detailsjson",
    metadata,
    Column(
        "credit_reversal",
        Treasury__CreditReversal,
        ForeignKey("Treasury__CreditReversal"),
        nullable=True,
    ),
    Column(
        "debit_reversal",
        Treasury__DebitReversal,
        ForeignKey("Treasury__DebitReversal"),
        nullable=True,
    ),
    Column(
        "inbound_transfer",
        Treasury__InboundTransfer,
        ForeignKey("Treasury__InboundTransfer"),
        nullable=True,
    ),
    Column(
        "issuing_authorization",
        Issuing__Authorization,
        ForeignKey("Issuing__Authorization"),
        nullable=True,
    ),
    Column(
        "outbound_payment",
        Treasury__OutboundPayment,
        ForeignKey("Treasury__OutboundPayment"),
        nullable=True,
    ),
    Column(
        "outbound_transfer",
        Treasury__OutboundTransfer,
        ForeignKey("Treasury__OutboundTransfer"),
        nullable=True,
    ),
    Column(
        "received_credit",
        Treasury__ReceivedCredit,
        ForeignKey("Treasury__ReceivedCredit"),
        nullable=True,
    ),
    Column(
        "received_debit",
        Treasury__ReceivedDebit,
        ForeignKey("Treasury__ReceivedDebit"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Type of the flow that created the Transaction. Set to the same value as `flow_type`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_transactions_resource_flow_details.json"]
