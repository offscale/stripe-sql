from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentFlowsAmountDetailsResourceTip(Base):
    __tablename__ = "payment_flows_amount_details_resource_tip"
    amount = Column(
        Integer,
        comment="Portion of the amount that corresponds to a tip",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "PaymentFlowsAmountDetailsResourceTip(amount={amount!r}, id={id!r})".format(
                amount=self.amount, id=self.id
            )
        )


__all__ = ["payment_flows_amount_details_resource_tip"]
