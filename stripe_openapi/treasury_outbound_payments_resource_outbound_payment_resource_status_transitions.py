from sqlalchemy import Column, Identity, Integer

from . import Base


class TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitions(Base):
    __tablename__ = "treasury_outbound_payments_resource_outbound_payment_resource_status_transitions"
    canceled_at = Column(
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `canceled`",
        nullable=True,
    )
    failed_at = Column(
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `failed`",
        nullable=True,
    )
    posted_at = Column(
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `posted`",
        nullable=True,
    )
    returned_at = Column(
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `returned`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitions(canceled_at={canceled_at!r}, failed_at={failed_at!r}, posted_at={posted_at!r}, returned_at={returned_at!r}, id={id!r})".format(
            canceled_at=self.canceled_at,
            failed_at=self.failed_at,
            posted_at=self.posted_at,
            returned_at=self.returned_at,
            id=self.id,
        )


__all__ = [
    "treasury_outbound_payments_resource_outbound_payment_resource_status_transitions"
]
