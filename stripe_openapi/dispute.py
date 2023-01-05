from sqlalchemy import Boolean, Column, Integer, String


class Dispute(Base):
    """
    A dispute occurs when a customer questions your charge with their card issuer.

    When this happens, you're given the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate. You can find more
    information about the dispute process in our [Disputes and
    Fraud](/docs/disputes) documentation.

    Related guide: [Disputes and Fraud](https://stripe.com/docs/disputes).

    """

    __tablename__ = "dispute"
    amount = Column(
        Integer,
        comment="Disputed amount. Usually the amount of the charge, but can differ (usually because of currency fluctuation or because only part of the order is disputed)",
    )
    balance_transactions = Column(
        list,
        comment="List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute",
    )
    charge = Column(Charge, comment="ID of the charge that was disputed")
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    evidence = Column(DisputeEvidence)
    evidence_details = Column(DisputeEvidenceDetails)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    is_charge_refundable = Column(
        Boolean,
        comment="If true, it is still possible to refund the disputed payment. Once the payment has been fully refunded, no further funds will be withdrawn from your Stripe account as a result of this dispute",
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    network_reason_code = Column(
        String, comment="Network-dependent reason code for the dispute", nullable=True
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    payment_intent = Column(
        PaymentIntent,
        comment="ID of the PaymentIntent that was disputed",
        nullable=True,
    )
    reason = Column(
        String,
        comment="Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Read more about [dispute reasons](https://stripe.com/docs/disputes/categories)",
    )
    status = Column(
        String,
        comment="Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `charge_refunded`, `won`, or `lost`",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Dispute(amount={amount!r}, balance_transactions={balance_transactions!r}, charge={charge!r}, created={created!r}, currency={currency!r}, evidence={evidence!r}, evidence_details={evidence_details!r}, id={id!r}, is_charge_refundable={is_charge_refundable!r}, livemode={livemode!r}, metadata={metadata!r}, network_reason_code={network_reason_code!r}, object={object!r}, payment_intent={payment_intent!r}, reason={reason!r}, status={status!r})".format(
            amount=self.amount,
            balance_transactions=self.balance_transactions,
            charge=self.charge,
            created=self.created,
            currency=self.currency,
            evidence=self.evidence,
            evidence_details=self.evidence_details,
            id=self.id,
            is_charge_refundable=self.is_charge_refundable,
            livemode=self.livemode,
            metadata=self.metadata,
            network_reason_code=self.network_reason_code,
            object=self.object,
            payment_intent=self.payment_intent,
            reason=self.reason,
            status=self.status,
        )


__all__ = ["dispute"]
