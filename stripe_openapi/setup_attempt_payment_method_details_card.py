from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsCard.Json = Table(
    "setup_attempt_payment_method_details_card.json",
    metadata,
    Column(
        "three_d_secure",
        ThreeDSecureDetails,
        ForeignKey("ThreeDSecureDetails"),
        comment="Populated if this authorization used 3D Secure authentication",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_card.json"]
