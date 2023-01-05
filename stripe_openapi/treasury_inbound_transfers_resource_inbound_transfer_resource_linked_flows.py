from sqlalchemy import Column, Integer, String


class Treasury_Inbound_Transfers_Resource_Inbound_Transfer_Resource_Linked_Flows(Base):
    __tablename__ = (
        "treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flows"
    )
    received_debit = Column(
        String,
        comment="If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Inbound_Transfers_Resource_Inbound_Transfer_Resource_Linked_Flows(received_debit={received_debit!r}, id={id!r})".format(
            received_debit=self.received_debit, id=self.id
        )


__all__ = ["treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flows"]
