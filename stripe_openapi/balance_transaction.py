from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table, list

from . import metadata

BalanceTransactionJson = Table(
    "balance_transactionjson",
    metadata,
    Column("amount", Integer, comment="Gross amount of the transaction, in %s"),
    Column(
        "available_on",
        Integer,
        comment="The date the transaction's net funds will become available in the Stripe balance",
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
        "exchange_rate",
        Float,
        comment="The exchange rate used, if applicable, for this transaction. Specifically, if money was converted from currency A to currency B, then the `amount` in currency A, times `exchange_rate`, would be the `amount` in currency B. For example, suppose you charged a customer 10.00 EUR. Then the PaymentIntent's `amount` would be `1000` and `currency` would be `eur`. Suppose this was converted into 12.34 USD in your Stripe account. Then the BalanceTransaction's `amount` would be `1234`, `currency` would be `usd`, and `exchange_rate` would be `1.234`",
        nullable=True,
    ),
    Column("fee", Integer, comment="Fees (in %s) paid for this transaction"),
    Column(
        "fee_details",
        list,
        comment="Detailed breakdown of fees (in %s) paid for this transaction",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("net", Integer, comment="Net amount of the transaction, in %s"),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "reporting_category",
        String,
        comment="[Learn more](https://stripe.com/docs/reports/reporting-categories) about how reporting categories can help you understand balance transactions from an accounting perspective",
    ),
    Column(
        "source",
        BalanceTransactionSource,
        ForeignKey("BalanceTransactionSource"),
        comment="The Stripe object to which this transaction is related",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="If the transaction's net funds are available in the Stripe balance yet. Either `available` or `pending`",
    ),
    Column(
        "type",
        String,
        comment="Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `payment`, `payment_failure_refund`, `payment_refund`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. [Learn more](https://stripe.com/docs/reports/balance-transaction-types) about balance transaction types and what they represent. If you are looking to classify transactions for accounting purposes, you might want to consider `reporting_category` instead",
    ),
)
__all__ = ["balance_transaction.json"]
