from sqlalchemy import Column, String


class Payment_Method_Details_Ach_Credit_Transfer(Base):
    __tablename__ = "payment_method_details_ach_credit_transfer"
    account_number = Column(
        String, comment="Account number to transfer funds to", nullable=True
    )
    bank_name = Column(
        String,
        comment="Name of the bank associated with the routing number",
        nullable=True,
        primary_key=True,
    )
    routing_number = Column(
        String,
        comment="Routing transit number for the bank account to transfer funds to",
        nullable=True,
    )
    swift_code = Column(
        String,
        comment="SWIFT code of the bank associated with the routing number",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Ach_Credit_Transfer(account_number={account_number!r}, bank_name={bank_name!r}, routing_number={routing_number!r}, swift_code={swift_code!r})".format(
            account_number=self.account_number,
            bank_name=self.bank_name,
            routing_number=self.routing_number,
            swift_code=self.swift_code,
        )


__all__ = ["payment_method_details_ach_credit_transfer"]
