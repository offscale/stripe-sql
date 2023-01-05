from sqlalchemy import Column, Integer, String


class Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Funded_Transaction_Resource_Bank_Transfer(
    Base
):
    __tablename__ = "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer"
    eu_bank_transfer = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer,
        nullable=True,
    )
    reference = Column(
        String,
        comment="The user-supplied reference field on the bank transfer",
        nullable=True,
    )
    type = Column(
        String,
        comment="The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Funded_Transaction_Resource_Bank_Transfer(eu_bank_transfer={eu_bank_transfer!r}, reference={reference!r}, type={type!r}, id={id!r})".format(
            eu_bank_transfer=self.eu_bank_transfer,
            reference=self.reference,
            type=self.type,
            id=self.id,
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer"
]
