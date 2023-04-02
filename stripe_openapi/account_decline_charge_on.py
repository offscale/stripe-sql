from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

AccountDeclineChargeOnJson = Table(
    "account_decline_charge_onjson",
    metadata,
    Column(
        "avs_failure",
        Boolean,
        comment="Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification",
    ),
    Column(
        "cvc_failure",
        Boolean,
        comment="Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_decline_charge_on.json"]
