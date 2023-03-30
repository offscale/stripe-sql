from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails.Json = Table(
    "treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details.json",
    metadata,
    Column("balance", String, comment="Set when `type` is `balance`", nullable=True),
    Column(
        "billing_details",
        TreasurySharedResourceBillingDetails,
        ForeignKey("TreasurySharedResourceBillingDetails"),
    ),
    Column(
        "financial_account",
        ReceivedPaymentMethodDetailsFinancialAccount,
        ForeignKey("ReceivedPaymentMethodDetailsFinancialAccount"),
        nullable=True,
    ),
    Column(
        "issuing_card",
        String,
        comment="Set when `type` is `issuing_card`. This is an [Issuing Card](https://stripe.com/docs/api#issuing_cards) ID",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Polymorphic type matching the originating money movement's source. This can be an external account, a Stripe balance, or a FinancialAccount",
    ),
    Column(
        "us_bank_account",
        TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccount,
        ForeignKey("TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details.json"
]
