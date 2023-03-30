from sqlalchemy import Column, String, Table

from . import metadata

CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer.Json = Table(
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer.json",
    metadata,
    Column(
        "bic",
        String,
        comment="The BIC of the bank of the sender of the funding",
        nullable=True,
    ),
    Column(
        "iban_last4",
        String,
        comment="The last 4 digits of the IBAN of the sender of the funding",
        nullable=True,
    ),
    Column(
        "sender_name",
        String,
        comment="The full name of the sender, as supplied by the sending bank",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer.json"
]
