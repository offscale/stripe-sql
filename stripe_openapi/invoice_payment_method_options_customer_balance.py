from sqlalchemy import Column, Integer, String


class Invoice_Payment_Method_Options_Customer_Balance(Base):
    __tablename__ = "invoice_payment_method_options_customer_balance"
    bank_transfer = Column(
        InvoicePaymentMethodOptionsCustomerBalanceBankTransfer, nullable=True
    )
    funding_type = Column(
        String,
        comment="The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Payment_Method_Options_Customer_Balance(bank_transfer={bank_transfer!r}, funding_type={funding_type!r}, id={id!r})".format(
            bank_transfer=self.bank_transfer, funding_type=self.funding_type, id=self.id
        )


__all__ = ["invoice_payment_method_options_customer_balance"]
