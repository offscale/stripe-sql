from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

OutboundPaymentsPaymentMethodDetailsJson = Table(
    "outbound_payments_payment_method_detailsjson",
    metadata,
    Column(
        "billing_details",
        TreasurySharedResourceBillingDetails,
        ForeignKey("TreasurySharedResourceBillingDetails"),
    ),
    Column(
        "financial_account",
        OutboundPaymentsPaymentMethodDetailsFinancialAccount,
        ForeignKey("OutboundPaymentsPaymentMethodDetailsFinancialAccount"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the payment method used in the OutboundPayment",
    ),
    Column(
        "us_bank_account",
        OutboundPaymentsPaymentMethodDetailsUsBankAccount,
        ForeignKey("OutboundPaymentsPaymentMethodDetailsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["outbound_payments_payment_method_details.json"]
