from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SetupAttemptPaymentMethodDetailsJson = Table(
    "setup_attempt_payment_method_detailsjson",
    metadata,
    Column(
        "acss_debit",
        SetupAttemptPaymentMethodDetailsAcssDebit,
        ForeignKey("SetupAttemptPaymentMethodDetailsAcssDebit"),
        nullable=True,
    ),
    Column(
        "au_becs_debit",
        SetupAttemptPaymentMethodDetailsAuBecsDebit,
        ForeignKey("SetupAttemptPaymentMethodDetailsAuBecsDebit"),
        nullable=True,
    ),
    Column(
        "bacs_debit",
        SetupAttemptPaymentMethodDetailsBacsDebit,
        ForeignKey("SetupAttemptPaymentMethodDetailsBacsDebit"),
        nullable=True,
    ),
    Column(
        "bancontact",
        SetupAttemptPaymentMethodDetailsBancontact,
        ForeignKey("SetupAttemptPaymentMethodDetailsBancontact"),
        nullable=True,
    ),
    Column(
        "blik",
        SetupAttemptPaymentMethodDetailsBlik,
        ForeignKey("SetupAttemptPaymentMethodDetailsBlik"),
        nullable=True,
    ),
    Column(
        "boleto",
        SetupAttemptPaymentMethodDetailsBoleto,
        ForeignKey("SetupAttemptPaymentMethodDetailsBoleto"),
        nullable=True,
    ),
    Column(
        "card",
        SetupAttemptPaymentMethodDetailsCard,
        ForeignKey("SetupAttemptPaymentMethodDetailsCard"),
        nullable=True,
    ),
    Column(
        "card_present",
        SetupAttemptPaymentMethodDetailsCardPresent,
        ForeignKey("SetupAttemptPaymentMethodDetailsCardPresent"),
        nullable=True,
    ),
    Column(
        "cashapp",
        SetupAttemptPaymentMethodDetailsCashapp,
        ForeignKey("SetupAttemptPaymentMethodDetailsCashapp"),
        nullable=True,
    ),
    Column(
        "ideal",
        SetupAttemptPaymentMethodDetailsIdeal,
        ForeignKey("SetupAttemptPaymentMethodDetailsIdeal"),
        nullable=True,
    ),
    Column(
        "klarna",
        SetupAttemptPaymentMethodDetailsKlarna,
        ForeignKey("SetupAttemptPaymentMethodDetailsKlarna"),
        nullable=True,
    ),
    Column(
        "link",
        SetupAttemptPaymentMethodDetailsLink,
        ForeignKey("SetupAttemptPaymentMethodDetailsLink"),
        nullable=True,
    ),
    Column(
        "sepa_debit",
        SetupAttemptPaymentMethodDetailsSepaDebit,
        ForeignKey("SetupAttemptPaymentMethodDetailsSepaDebit"),
        nullable=True,
    ),
    Column(
        "sofort",
        SetupAttemptPaymentMethodDetailsSofort,
        ForeignKey("SetupAttemptPaymentMethodDetailsSofort"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the payment method used in the SetupIntent (e.g., `card`). An additional hash is included on `payment_method_details` with a name matching this value. It contains confirmation-specific information for the payment method",
    ),
    Column(
        "us_bank_account",
        SetupAttemptPaymentMethodDetailsUsBankAccount,
        ForeignKey("SetupAttemptPaymentMethodDetailsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details.json"]
