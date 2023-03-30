from sqlalchemy import Column, String, Table

from . import metadata

ReceivedPaymentMethodDetailsFinancialAccount.Json = Table(
    "received_payment_method_details_financial_account.json",
    metadata,
    Column("id", String, comment="The FinancialAccount ID", primary_key=True),
    Column(
        "network",
        String,
        comment="The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`",
    ),
)
__all__ = ["received_payment_method_details_financial_account.json"]
