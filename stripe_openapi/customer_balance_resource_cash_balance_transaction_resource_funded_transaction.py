from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction(Base):
    __tablename__ = (
        "customer_balance_resource_cash_balance_transaction_resource_funded_transaction"
    )
    bank_transfer = Column(
        Integer,
        ForeignKey(
            "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer.id"
        ),
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction(bank_transfer={bank_transfer!r}, id={id!r})".format(
            bank_transfer=self.bank_transfer, id=self.id
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction"
]
