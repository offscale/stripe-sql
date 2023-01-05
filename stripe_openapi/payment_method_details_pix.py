from sqlalchemy import Column, String


class Payment_Method_Details_Pix(Base):
    __tablename__ = "payment_method_details_pix"
    bank_transaction_id = Column(
        String,
        comment="Unique transaction id generated by BCB",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Pix(bank_transaction_id={bank_transaction_id!r})".format(
            bank_transaction_id=self.bank_transaction_id
        )


__all__ = ["payment_method_details_pix"]
