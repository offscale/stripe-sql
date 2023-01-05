from sqlalchemy import Column, Integer, String


class Payment_Method_Details_Giropay(Base):
    __tablename__ = "payment_method_details_giropay"
    bank_code = Column(
        String,
        comment="Bank code of bank associated with the bank account",
        nullable=True,
    )
    bank_name = Column(
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
    )
    bic = Column(
        String,
        comment="Bank Identifier Code of the bank associated with the bank account",
        nullable=True,
    )
    verified_name = Column(
        String,
        comment="Owner's verified full name. Values are verified or provided by Giropay directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated.\nGiropay rarely provides this information so the attribute is usually empty",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Giropay(bank_code={bank_code!r}, bank_name={bank_name!r}, bic={bic!r}, verified_name={verified_name!r}, id={id!r})".format(
            bank_code=self.bank_code,
            bank_name=self.bank_name,
            bic=self.bic,
            verified_name=self.verified_name,
            id=self.id,
        )


__all__ = ["payment_method_details_giropay"]
