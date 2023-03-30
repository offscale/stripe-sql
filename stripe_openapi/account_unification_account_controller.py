from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

AccountUnificationAccountController.Json = Table(
    "account_unification_account_controller.json",
    metadata,
    Column(
        "is_controller",
        Boolean,
        comment="`true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts). Otherwise, this field is null",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_unification_account_controller.json"]
