from sqlalchemy import Column, Integer, String


class Payment_Method_Details_Afterpay_Clearpay(Base):
    __tablename__ = "payment_method_details_afterpay_clearpay"
    reference = Column(
        String,
        comment="Order identifier shown to the merchant in Afterpay’s online portal",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Afterpay_Clearpay(reference={reference!r}, id={id!r})".format(
            reference=self.reference, id=self.id
        )


__all__ = ["payment_method_details_afterpay_clearpay"]
