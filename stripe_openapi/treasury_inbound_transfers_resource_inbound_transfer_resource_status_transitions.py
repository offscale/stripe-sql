from sqlalchemy import Column, Integer


class Treasury_Inbound_Transfers_Resource_Inbound_Transfer_Resource_Status_Transitions(
    Base
):
    __tablename__ = "treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions"
    canceled_at = Column(
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `canceled`",
        nullable=True,
    )
    failed_at = Column(
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `failed`",
        nullable=True,
    )
    succeeded_at = Column(
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `succeeded`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Inbound_Transfers_Resource_Inbound_Transfer_Resource_Status_Transitions(canceled_at={canceled_at!r}, failed_at={failed_at!r}, succeeded_at={succeeded_at!r}, id={id!r})".format(
            canceled_at=self.canceled_at,
            failed_at=self.failed_at,
            succeeded_at=self.succeeded_at,
            id=self.id,
        )


__all__ = [
    "treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions"
]
