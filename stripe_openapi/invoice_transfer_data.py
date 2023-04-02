from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.account import Account

from . import metadata

InvoiceTransferDataJson = Table(
    "invoice_transfer_datajson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount in %s that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination",
        nullable=True,
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="The account where funds from the payment will be transferred to upon payment success",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_transfer_data.json"]
