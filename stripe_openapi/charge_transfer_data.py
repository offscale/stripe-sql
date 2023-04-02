from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.account import Account

from . import metadata

ChargeTransferDataJson = Table(
    "charge_transfer_datajson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account",
        nullable=True,
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["charge_transfer_data.json"]
