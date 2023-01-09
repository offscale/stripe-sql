from sqlalchemy import Column, Identity, Integer, String

from . import Base


class TreasuryOutboundPaymentsResourceReturnedStatus(Base):
    __tablename__ = "treasury_outbound_payments_resource_returned_status"
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
        return "TreasuryOutboundPaymentsResourceReturnedStatus(code={code!r}, transaction={transaction!r}, id={id!r})".format(
            code=self.code, transaction=self.transaction, id=self.id
        )


__all__ = ["treasury_outbound_payments_resource_returned_status"]
