from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class Charge(Base):
    """
    To charge a credit or a debit card, you create a `Charge` object. You can

    retrieve and refund individual charges as well as list all charges. Charges
    are identified by a unique, random ID.

    Related guide: [Accept a payment with the Charges API](https://stripe.com/docs/payments/accept-a-payment-charges).

    """

    __tablename__ = "charge"
    alternate_statement_descriptors = Column(
        Integer, ForeignKey("alternate_statement_descriptors.id"), nullable=True
    )
    amount = Column(
        Integer,
        comment="Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)",
    )
    amount_captured = Column(
        Integer,
        comment="Amount in %s captured (can be less than the amount attribute on the charge if a partial capture was made)",
    )
    amount_refunded = Column(
        Integer,
        comment="Amount in %s refunded (can be less than the amount attribute on the charge if a partial refund was issued)",
    )
    application = Column(
        Application,
        ForeignKey("Application"),
        comment="ID of the Connect application that created the charge",
        nullable=True,
    )
    application_fee = Column(
        String,
        ForeignKey("application_fee.id"),
        comment="The application fee (if any) for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details",
        nullable=True,
    )
    application_fee_amount = Column(
        Integer,
        comment="The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details",
        nullable=True,
    )
    authorization_code = Column(
        String, comment="Authorization code on the charge", nullable=True
    )
    balance_transaction = Column(
        String,
        ForeignKey("balance_transaction.id"),
        comment="ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes)",
        nullable=True,
    )
    billing_details = Column(Integer, ForeignKey("billing_details.id"))
    calculated_statement_descriptor = Column(
        String,
        comment="The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined",
        nullable=True,
    )
    captured = Column(
        Boolean,
        comment="If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="ID of the customer this charge is for if one exists",
        nullable=True,
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    destination = Column(
        Account,
        ForeignKey("Account"),
        comment="ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request",
        nullable=True,
    )
    dispute = Column(
        Dispute,
        ForeignKey("Dispute"),
        comment="Details about the dispute if the charge has been disputed",
        nullable=True,
    )
    disputed = Column(Boolean, comment="Whether the charge has been disputed")
    failure_balance_transaction = Column(
        String,
        ForeignKey("balance_transaction.id"),
        comment="ID of the balance transaction that describes the reversal of the balance on your account due to payment failure",
        nullable=True,
    )
    failure_code = Column(
        String,
        comment="Error code explaining reason for charge failure if available (see [the errors section](https://stripe.com/docs/error-codes) for a list of codes)",
        nullable=True,
    )
    failure_message = Column(
        String,
        comment="Message to user further explaining reason for charge failure if available",
        nullable=True,
    )
    fraud_details = Column(
        Integer,
        ForeignKey("charge_fraud_details.id"),
        comment="Information on fraud assessments for the charge",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice = Column(
        Invoice,
        ForeignKey("Invoice"),
        comment="ID of the invoice this charge is for if one exists",
        nullable=True,
    )
    level3 = Column(Level3, ForeignKey("Level3"), nullable=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    on_behalf_of = Column(
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers) for details",
        nullable=True,
    )
    outcome = Column(
        Integer,
        ForeignKey("charge_outcome.id"),
        comment="Details about whether the payment was accepted, and why. See [understanding declines](https://stripe.com/docs/declines) for details",
        nullable=True,
    )
    paid = Column(
        Boolean,
        comment="`true` if the charge succeeded, or was successfully authorized for later capture",
    )
    payment_intent = Column(
        String,
        ForeignKey("payment_intent.id"),
        comment="ID of the PaymentIntent associated with this charge, if one exists",
        nullable=True,
    )
    payment_method = Column(
        String, comment="ID of the payment method used in this charge", nullable=True
    )
    payment_method_details = Column(
        Integer,
        ForeignKey("payment_method_details.id"),
        comment="Details about the payment method at the time of the transaction",
        nullable=True,
    )
    radar_options = Column(Integer, ForeignKey("radar_radar_options.id"), nullable=True)
    receipt_email = Column(
        String,
        comment="This is the email address that the receipt for this charge was sent to",
        nullable=True,
    )
    receipt_number = Column(
        String,
        comment="This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent",
        nullable=True,
    )
    receipt_url = Column(
        String,
        comment="This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt",
        nullable=True,
    )
    refunded = Column(
        Boolean,
        comment="Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false",
    )
    refunds = Column(
        JSON,
        comment="A list of refunds that have been applied to the charge",
        nullable=True,
    )
    review = Column(
        Review,
        ForeignKey("Review"),
        comment="ID of the review associated with this charge if one exists",
        nullable=True,
    )
    shipping = Column(
        Shipping,
        ForeignKey("Shipping"),
        comment="Shipping information for the charge",
        nullable=True,
    )
    source = Column(
        Integer,
        ForeignKey("payment_source.id"),
        comment="This is a legacy field that will be removed in the future. It contains the Source, Card, or BankAccount object used for the charge. For details about the payment method used for this charge, refer to `payment_method` or `payment_method_details` instead",
        nullable=True,
    )
    source_transfer = Column(
        Transfer,
        ForeignKey("Transfer"),
        comment="The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details",
        nullable=True,
    )
    statement_descriptor = Column(
        String,
        comment="For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters",
        nullable=True,
    )
    statement_descriptor_suffix = Column(
        String,
        comment="Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor",
        nullable=True,
    )
    status = Column(
        String,
        comment="The status of the payment is either `succeeded`, `pending`, or `failed`",
    )
    transfer = Column(
        Transfer,
        ForeignKey("Transfer"),
        comment="ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter)",
        nullable=True,
    )
    transfer_data = Column(
        Integer,
        ForeignKey("charge_transfer_data.id"),
        comment="An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details",
        nullable=True,
    )
    transfer_group = Column(
        String,
        comment="A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers#transfer-options) for details",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Charge(alternate_statement_descriptors={alternate_statement_descriptors!r}, amount={amount!r}, amount_captured={amount_captured!r}, amount_refunded={amount_refunded!r}, application={application!r}, application_fee={application_fee!r}, application_fee_amount={application_fee_amount!r}, authorization_code={authorization_code!r}, balance_transaction={balance_transaction!r}, billing_details={billing_details!r}, calculated_statement_descriptor={calculated_statement_descriptor!r}, captured={captured!r}, created={created!r}, currency={currency!r}, customer={customer!r}, description={description!r}, destination={destination!r}, dispute={dispute!r}, disputed={disputed!r}, failure_balance_transaction={failure_balance_transaction!r}, failure_code={failure_code!r}, failure_message={failure_message!r}, fraud_details={fraud_details!r}, id={id!r}, invoice={invoice!r}, level3={level3!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, outcome={outcome!r}, paid={paid!r}, payment_intent={payment_intent!r}, payment_method={payment_method!r}, payment_method_details={payment_method_details!r}, radar_options={radar_options!r}, receipt_email={receipt_email!r}, receipt_number={receipt_number!r}, receipt_url={receipt_url!r}, refunded={refunded!r}, refunds={refunds!r}, review={review!r}, shipping={shipping!r}, source={source!r}, source_transfer={source_transfer!r}, statement_descriptor={statement_descriptor!r}, statement_descriptor_suffix={statement_descriptor_suffix!r}, status={status!r}, transfer={transfer!r}, transfer_data={transfer_data!r}, transfer_group={transfer_group!r})".format(
            alternate_statement_descriptors=self.alternate_statement_descriptors,
            amount=self.amount,
            amount_captured=self.amount_captured,
            amount_refunded=self.amount_refunded,
            application=self.application,
            application_fee=self.application_fee,
            application_fee_amount=self.application_fee_amount,
            authorization_code=self.authorization_code,
            balance_transaction=self.balance_transaction,
            billing_details=self.billing_details,
            calculated_statement_descriptor=self.calculated_statement_descriptor,
            captured=self.captured,
            created=self.created,
            currency=self.currency,
            customer=self.customer,
            description=self.description,
            destination=self.destination,
            dispute=self.dispute,
            disputed=self.disputed,
            failure_balance_transaction=self.failure_balance_transaction,
            failure_code=self.failure_code,
            failure_message=self.failure_message,
            fraud_details=self.fraud_details,
            id=self.id,
            invoice=self.invoice,
            level3=self.level3,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            on_behalf_of=self.on_behalf_of,
            outcome=self.outcome,
            paid=self.paid,
            payment_intent=self.payment_intent,
            payment_method=self.payment_method,
            payment_method_details=self.payment_method_details,
            radar_options=self.radar_options,
            receipt_email=self.receipt_email,
            receipt_number=self.receipt_number,
            receipt_url=self.receipt_url,
            refunded=self.refunded,
            refunds=self.refunds,
            review=self.review,
            shipping=self.shipping,
            source=self.source,
            source_transfer=self.source_transfer,
            statement_descriptor=self.statement_descriptor,
            statement_descriptor_suffix=self.statement_descriptor_suffix,
            status=self.status,
            transfer=self.transfer,
            transfer_data=self.transfer_data,
            transfer_group=self.transfer_group,
        )


__all__ = ["charge"]
