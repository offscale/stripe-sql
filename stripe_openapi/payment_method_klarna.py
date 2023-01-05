from sqlalchemy import Column, Integer


class Payment_Method_Klarna(Base):
    __tablename__ = "payment_method_klarna"
    dob = Column(
        PaymentFlowsPrivatePaymentMethodsKlarnaDob,
        comment="The customer's date of birth, if provided",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Klarna(dob={dob!r}, id={id!r})".format(
            dob=self.dob, id=self.id
        )


__all__ = ["payment_method_klarna"]
