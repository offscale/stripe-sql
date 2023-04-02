from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
    list,
)

from . import metadata

BalanceJson = Table(
    "balancejson",
    metadata,
    Column(
        "available",
        list,
        comment="Funds that are available to be transferred or paid out, whether automatically by Stripe or explicitly via the [Transfers API](https://stripe.com/docs/api#transfers) or [Payouts API](https://stripe.com/docs/api#payouts). The available balance for each currency and payment type can be found in the `source_types` property",
    ),
    Column(
        "connect_reserved",
        list,
        comment="Funds held due to negative balances on connected Custom accounts. The connect reserve balance for each currency and payment type can be found in the `source_types` property",
        nullable=True,
    ),
    Column(
        "instant_available",
        list,
        comment="Funds that can be paid out using Instant Payouts",
        nullable=True,
    ),
    Column("issuing", BalanceDetail, ForeignKey("BalanceDetail"), nullable=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "pending",
        list,
        comment="Funds that are not yet available in the balance, due to the 7-day rolling pay cycle. The pending balance for each currency, and for each payment type, can be found in the `source_types` property",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance.json"]
