from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

MandatePaymentMethodDetails.Json = Table(
    "mandate_payment_method_details.json",
    metadata,
    Column(
        "acss_debit", MandateAcssDebit, ForeignKey("MandateAcssDebit"), nullable=True
    ),
    Column(
        "au_becs_debit",
        MandateAuBecsDebit,
        ForeignKey("MandateAuBecsDebit"),
        nullable=True,
    ),
    Column(
        "bacs_debit", MandateBacsDebit, ForeignKey("MandateBacsDebit"), nullable=True
    ),
    Column("blik", MandateBlik, ForeignKey("MandateBlik"), nullable=True),
    Column(
        "card",
        CardMandatePaymentMethodDetails,
        ForeignKey("CardMandatePaymentMethodDetails"),
        nullable=True,
    ),
    Column("cashapp", MandateCashapp, ForeignKey("MandateCashapp"), nullable=True),
    Column("link", MandateLink, ForeignKey("MandateLink"), nullable=True),
    Column(
        "sepa_debit", MandateSepaDebit, ForeignKey("MandateSepaDebit"), nullable=True
    ),
    Column(
        "type",
        String,
        comment="The type of the payment method associated with this mandate. An additional hash is included on `payment_method_details` with a name matching this value. It contains mandate information specific to the payment method",
    ),
    Column(
        "us_bank_account",
        MandateUsBankAccount,
        ForeignKey("MandateUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_payment_method_details.json"]
