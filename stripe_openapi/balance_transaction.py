from sqlalchemy import Column, Float, Integer, String


class Balance_Transaction(Base):
    """
    Balance transactions represent funds moving through your Stripe account.

    They're created for every type of transaction that comes into or flows out of your Stripe account balance.

    Related guide: [Balance Transaction Types](https://stripe.com/docs/reports/balance-transaction-types).

    """

    __tablename__ = "balance_transaction"
    amount = Column(Integer, comment="Gross amount of the transaction, in %s")
    available_on = Column(
        Integer,
        comment="The date the transaction's net funds will become available in the Stripe balance",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    exchange_rate = Column(
        Float,
        comment="The exchange rate used, if applicable, for this transaction. Specifically, if money was converted from currency A to currency B, then the `amount` in currency A, times `exchange_rate`, would be the `amount` in currency B. For example, suppose you charged a customer 10.00 EUR. Then the PaymentIntent's `amount` would be `1000` and `currency` would be `eur`. Suppose this was converted into 12.34 USD in your Stripe account. Then the BalanceTransaction's `amount` would be `1234`, `currency` would be `usd`, and `exchange_rate` would be `1.234`",
        nullable=True,
    )
    fee = Column(Integer, comment="Fees (in %s) paid for this transaction")
    fee_details = Column(
        list, comment="Detailed breakdown of fees (in %s) paid for this transaction"
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    net = Column(Integer, comment="Net amount of the transaction, in %s")
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    reporting_category = Column(
        String,
        comment="[Learn more](https://stripe.com/docs/reports/reporting-categories) about how reporting categories can help you understand balance transactions from an accounting perspective",
    )
    source = Column(
        balance_transaction_source,
        comment="[[FK(balance_transaction_source)]] The Stripe object to which this transaction is related",
        nullable=True,
    )
    status = Column(
        String,
        comment="If the transaction's net funds are available in the Stripe balance yet. Either `available` or `pending`",
    )
    type = Column(
        String,
        comment="Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `payment`, `payment_failure_refund`, `payment_refund`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. [Learn more](https://stripe.com/docs/reports/balance-transaction-types) about balance transaction types and what they represent. If you are looking to classify transactions for accounting purposes, you might want to consider `reporting_category` instead",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Balance_Transaction(amount={amount!r}, available_on={available_on!r}, created={created!r}, currency={currency!r}, description={description!r}, exchange_rate={exchange_rate!r}, fee={fee!r}, fee_details={fee_details!r}, id={id!r}, net={net!r}, object={object!r}, reporting_category={reporting_category!r}, source={source!r}, status={status!r}, type={type!r})".format(
            amount=self.amount,
            available_on=self.available_on,
            created=self.created,
            currency=self.currency,
            description=self.description,
            exchange_rate=self.exchange_rate,
            fee=self.fee,
            fee_details=self.fee_details,
            id=self.id,
            net=self.net,
            object=self.object,
            reporting_category=self.reporting_category,
            source=self.source,
            status=self.status,
            type=self.type,
        )


__all__ = ["balance_transaction"]
