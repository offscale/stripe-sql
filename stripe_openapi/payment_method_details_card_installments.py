from sqlalchemy import Column, Integer


class Payment_Method_Details_Card_Installments(Base):
    __tablename__ = "payment_method_details_card_installments"
    plan = Column(
        PaymentMethodDetailsCardInstallmentsPlan,
        comment="Installment plan selected for the payment",
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
            "Payment_Method_Details_Card_Installments(plan={plan!r}, id={id!r})".format(
                plan=self.plan, id=self.id
            )
        )


__all__ = ["payment_method_details_card_installments"]
