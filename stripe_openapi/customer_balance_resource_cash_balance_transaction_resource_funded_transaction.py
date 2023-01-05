from sqlalchemy import Column, Integer


class Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Funded_Transaction(
    Base
):
    __tablename__ = (
        "customer_balance_resource_cash_balance_transaction_resource_funded_transaction"
    )
    bank_transfer = Column(
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Funded_Transaction(bank_transfer={bank_transfer!r}, id={id!r})".format(
            bank_transfer=self.bank_transfer, id=self.id
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction"
]
