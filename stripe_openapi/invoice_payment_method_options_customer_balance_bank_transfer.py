from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

InvoicePaymentMethodOptionsCustomerBalanceBankTransfer.Json = Table(
    "invoice_payment_method_options_customer_balance_bank_transfer.json",
    metadata,
    Column(
        "eu_bank_transfer",
        InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        ForeignKey(
            "InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
        ),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_payment_method_options_customer_balance_bank_transfer.json"]
