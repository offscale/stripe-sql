from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

ChargeFraudDetails.Json = Table(
    "charge_fraud_details.json",
    metadata,
    Column(
        "stripe_report",
        String,
        comment="Assessments from Stripe. If set, the value is `fraudulent`",
        nullable=True,
    ),
    Column(
        "user_report",
        String,
        comment="Assessments reported by you. If set, possible values of are `safe` and `fraudulent`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["charge_fraud_details.json"]
