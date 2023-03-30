from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.account import Account

from . import metadata

PaymentLinksResourceTransferData.Json = Table(
    "payment_links_resource_transfer_data.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount in %s that will be transferred to the destination account. By default, the entire amount is transferred to the destination",
        nullable=True,
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="The connected account receiving the transfer",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_transfer_data.json"]
