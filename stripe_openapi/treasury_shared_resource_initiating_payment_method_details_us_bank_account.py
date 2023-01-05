from sqlalchemy import Column, String


class Treasury_Shared_Resource_Initiating_Payment_Method_Details_Us_Bank_Account(Base):
    __tablename__ = (
        "treasury_shared_resource_initiating_payment_method_details_us_bank_account"
    )
    bank_name = Column(String, comment="Bank name", nullable=True, primary_key=True)
    last4 = Column(
        String, comment="The last four digits of the bank account number", nullable=True
    )
    routing_number = Column(
        String, comment="The routing number for the bank account", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Shared_Resource_Initiating_Payment_Method_Details_Us_Bank_Account(bank_name={bank_name!r}, last4={last4!r}, routing_number={routing_number!r})".format(
            bank_name=self.bank_name,
            last4=self.last4,
            routing_number=self.routing_number,
        )


__all__ = ["treasury_shared_resource_initiating_payment_method_details_us_bank_account"]
