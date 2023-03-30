from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

BalanceAmount.Json = Table(
    "balance_amount.json",
    metadata,
    Column("amount", Integer, comment="Balance amount"),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "source_types",
        BalanceAmountBySourceType,
        ForeignKey("BalanceAmountBySourceType"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance_amount.json"]
