from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer.Json = Table(
    "invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer.json",
    metadata,
    Column(
        "country",
        String,
        comment="The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer.json"
]
