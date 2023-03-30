from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

AccountPayoutSettings.Json = Table(
    "account_payout_settings.json",
    metadata,
    Column(
        "debit_negative_balances",
        Boolean,
        comment="A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See our [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances) documentation for details. Default value is `false` for Custom accounts, otherwise `true`",
    ),
    Column("schedule", TransferSchedule, ForeignKey("TransferSchedule")),
    Column(
        "statement_descriptor",
        String,
        comment="The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_payout_settings.json"]
