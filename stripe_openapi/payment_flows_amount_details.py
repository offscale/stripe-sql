from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentFlowsAmountDetails(Base):
    __tablename__ = "payment_flows_amount_details"
    tip = Column(
        Integer,
        ForeignKey("payment_flows_amount_details_resource_tip.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentFlowsAmountDetails(tip={tip!r}, id={id!r})".format(
            tip=self.tip, id=self.id
        )


__all__ = ["payment_flows_amount_details"]
