from sqlalchemy import Column, Identity, Integer, String

from . import Base


class TreasuryOutboundTransfersResourceReturnedDetails(Base):
    __tablename__ = "treasury_outbound_transfers_resource_returned_details"
    code = Column(String, comment="Reason for the return")
    transaction = Column(
        Treasury.Transaction,
        comment="[[FK(Treasury.Transaction)]] The Transaction associated with this object",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryOutboundTransfersResourceReturnedDetails(code={code!r}, transaction={transaction!r}, id={id!r})".format(
            code=self.code, transaction=self.transaction, id=self.id
        )


__all__ = ["treasury_outbound_transfers_resource_returned_details"]
