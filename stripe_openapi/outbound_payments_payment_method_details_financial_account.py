from sqlalchemy import Column, String, Table

from . import metadata

OutboundPaymentsPaymentMethodDetailsFinancialAccountJson = Table(
    "outbound_payments_payment_method_details_financial_accountjson",
    metadata,
    Column("id", String, comment="Token of the FinancialAccount", primary_key=True),
    Column("network", String, comment="The rails used to send funds"),
)
__all__ = ["outbound_payments_payment_method_details_financial_account.json"]
