from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionJson = Table(
    "customer_balance_resource_cash_balance_transaction_resource_funded_transactionjson",
    metadata,
    Column(
        "bank_transfer",
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer"
        ),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction.json"
]
