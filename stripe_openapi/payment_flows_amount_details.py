from sqlalchemy import Column, Integer


class Payment_Flows_Amount_Details(Base):
    __tablename__ = "payment_flows_amount_details"
    tip = Column(PaymentFlowsAmountDetailsResourceTip, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Flows_Amount_Details(tip={tip!r}, id={id!r})".format(
            tip=self.tip, id=self.id
        )


__all__ = ["payment_flows_amount_details"]
