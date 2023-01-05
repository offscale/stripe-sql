from sqlalchemy import Column, Integer, String


class Payment_Method_Details_Card_Installments_Plan(Base):
    __tablename__ = "payment_method_details_card_installments_plan"
    count = Column(
        Integer,
        comment="For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card",
        nullable=True,
    )
    interval = Column(
        String,
        comment="For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card.\nOne of `month`",
        nullable=True,
    )
    type = Column(String, comment="Type of installment plan, one of `fixed_count`")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Card_Installments_Plan(count={count!r}, interval={interval!r}, type={type!r}, id={id!r})".format(
            count=self.count, interval=self.interval, type=self.type, id=self.id
        )


__all__ = ["payment_method_details_card_installments_plan"]
