from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.customer import Customer

from . import metadata

CustomerCashBalanceTransactionJson = Table(
    "customer_cash_balance_transactionjson",
    metadata,
    Column(
        "applied_to_payment",
        CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction"
        ),
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
        "customer",
        Customer,
        ForeignKey("Customer"),
        comment="The customer whose available cash balance changed as a result of this transaction",
    ),
    Column(
        "ending_balance",
        Integer,
        comment="The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column(
        "funded",
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction"
        ),
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "net_amount",
        Integer,
        comment="The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "refunded_from_payment",
        CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction"
        ),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the cash balance transaction. One of `applied_to_payment`, `unapplied_from_payment`, `refunded_from_payment`, `funded`, `return_initiated`, or `return_canceled`. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types",
    ),
    Column(
        "unapplied_from_payment",
        CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction,
        ForeignKey(
            "CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction"
        ),
        nullable=True,
    ),
)
__all__ = ["customer_cash_balance_transaction.json"]
