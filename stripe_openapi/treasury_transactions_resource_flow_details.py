from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from stripe_openapi.treasury__credit_reversal import Treasury__CreditReversal
from stripe_openapi.treasury__debit_reversal import Treasury__DebitReversal
from stripe_openapi.treasury__inbound_transfer import Treasury__InboundTransfer
from stripe_openapi.treasury__outbound_payment import Treasury__OutboundPayment
from stripe_openapi.treasury__outbound_transfer import Treasury__OutboundTransfer
from stripe_openapi.treasury__received_credit import Treasury__ReceivedCredit
from stripe_openapi.treasury__received_debit import Treasury__ReceivedDebit

from . import Base


class TreasuryTransactionsResourceFlowDetails(Base):
    __tablename__ = "treasury_transactions_resource_flow_details"
    credit_reversal = Column(
        Treasury__CreditReversal, ForeignKey("Treasury__CreditReversal"), nullable=True
    )
    debit_reversal = Column(
        Treasury__DebitReversal, ForeignKey("Treasury__DebitReversal"), nullable=True
    )
    inbound_transfer = Column(
        Treasury__InboundTransfer,
        ForeignKey("Treasury__InboundTransfer"),
        nullable=True,
    )
    issuing_authorization = Column(
        Issuing__Authorization, ForeignKey("Issuing__Authorization"), nullable=True
    )
    outbound_payment = Column(
        Treasury__OutboundPayment,
        ForeignKey("Treasury__OutboundPayment"),
        nullable=True,
    )
    outbound_transfer = Column(
        Treasury__OutboundTransfer,
        ForeignKey("Treasury__OutboundTransfer"),
        nullable=True,
    )
    received_credit = Column(
        Treasury__ReceivedCredit, ForeignKey("Treasury__ReceivedCredit"), nullable=True
    )
    received_debit = Column(
        Treasury__ReceivedDebit, ForeignKey("Treasury__ReceivedDebit"), nullable=True
    )
    type = Column(
        String,
        comment="Type of the flow that created the Transaction. Set to the same value as `flow_type`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryTransactionsResourceFlowDetails(credit_reversal={credit_reversal!r}, debit_reversal={debit_reversal!r}, inbound_transfer={inbound_transfer!r}, issuing_authorization={issuing_authorization!r}, outbound_payment={outbound_payment!r}, outbound_transfer={outbound_transfer!r}, received_credit={received_credit!r}, received_debit={received_debit!r}, type={type!r}, id={id!r})".format(
            credit_reversal=self.credit_reversal,
            debit_reversal=self.debit_reversal,
            inbound_transfer=self.inbound_transfer,
            issuing_authorization=self.issuing_authorization,
            outbound_payment=self.outbound_payment,
            outbound_transfer=self.outbound_transfer,
            received_credit=self.received_credit,
            received_debit=self.received_debit,
            type=self.type,
            id=self.id,
        )


__all__ = ["treasury_transactions_resource_flow_details"]
