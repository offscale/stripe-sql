from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer.Json = Table(
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer.json",
    metadata,
    Column(
        "eu_bank_transfer",
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer"
        ),
        nullable=True,
    ),
    Column(
        "reference",
        String,
        comment="The user-supplied reference field on the bank transfer",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer.json"
]
