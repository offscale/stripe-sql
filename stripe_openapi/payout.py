from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.payout import Payout

from . import metadata

PayoutJson = Table(
    "payoutjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Amount (in %s) to be transferred to your bank account or debit card",
    ),
    Column(
        "arrival_date",
        Integer,
        comment="Date the payout is expected to arrive in the bank. This factors in delays like weekends or bank holidays",
    ),
    Column(
        "automatic",
        Boolean,
        comment="Returns `true` if the payout was created by an [automated payout schedule](https://stripe.com/docs/payouts#payout-schedule), and `false` if it was [requested manually](https://stripe.com/docs/payouts#manual-payouts)",
    ),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="ID of the balance transaction that describes the impact of this payout on your account balance",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "destination",
        ExternalAccount,
        ForeignKey("DeletedExternalAccount"),
        comment="ID of the bank account or card the payout was sent to",
        nullable=True,
    ),
    Column(
        "failure_balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="If the payout failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance",
        nullable=True,
    ),
    Column(
        "failure_code",
        String,
        comment="Error code explaining reason for payout failure if available. See [Types of payout failures](https://stripe.com/docs/api#payout_failures) for a list of failure codes",
        nullable=True,
    ),
    Column(
        "failure_message",
        String,
        comment="Message to user further explaining reason for payout failure if available",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "method",
        String,
        comment="The method used to send this payout, which can be `standard` or `instant`. `instant` is only supported for payouts to debit cards. (See [Instant payouts for marketplaces](https://stripe.com/blog/instant-payouts-for-marketplaces) for more information.)",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "original_payout",
        Payout,
        ForeignKey("Payout"),
        comment="If the payout reverses another, this is the ID of the original payout",
        nullable=True,
    ),
    Column(
        "reconciliation_status",
        String,
        comment="If `completed`, the [Balance Transactions API](https://stripe.com/docs/api/balance_transactions/list#balance_transaction_list-payout) may be used to list all Balance Transactions that were paid out in this payout",
    ),
    Column(
        "reversed_by",
        Payout,
        ForeignKey("Payout"),
        comment="If the payout was reversed, this is the ID of the payout that reverses this payout",
        nullable=True,
    ),
    Column(
        "source_type",
        String,
        comment="The source balance this payout came from. One of `card`, `fpx`, or `bank_account`",
    ),
    Column(
        "statement_descriptor",
        String,
        comment="Extra information about a payout to be displayed on the user's bank statement",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it is submitted to the bank, when it becomes `in_transit`. The status then changes to `paid` if the transaction goes through, or to `failed` or `canceled` (within 5 business days). Some failed payouts may initially show as `paid` but then change to `failed`",
    ),
    Column("type", String, comment="Can be `bank_account` or `card`"),
)
__all__ = ["payout.json"]
