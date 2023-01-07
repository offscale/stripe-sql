from sqlalchemy import Boolean, Column, Integer, String


class Credit_Note(Base):
    """
    Issue a credit note to adjust an invoice's amount after the invoice is finalized.

    Related guide: [Credit Notes](https://stripe.com/docs/billing/invoices/credit-notes).

    """

    __tablename__ = "credit_note"
    amount = Column(
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, including tax",
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
        string | customer, comment="[[FK(deleted_customer)]] ID of the customer"
    )
    customer_balance_transaction = Column(
        customer_balance_transaction,
        comment="[[FK(customer_balance_transaction)]] Customer balance transaction related to this credit note",
        nullable=True,
    )
    discount_amount = Column(
        Integer,
        comment="The integer amount in %s representing the total amount of discount that was credited",
    )
    discount_amounts = Column(
        list, comment="The aggregate amounts calculated per discount for all line items"
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice = Column(invoice, comment="[[FK(invoice)]] ID of the invoice")
    lines = Column(JSON, comment="Line items that make up the credit note")
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    memo = Column(
        String,
        comment="Customer-facing text that appears on the credit note PDF",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    number = Column(
        String,
        comment="A unique number that identifies this particular credit note and appears on the PDF of the credit note and its associated invoice",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    out_of_band_amount = Column(
        Integer, comment="Amount that was credited outside of Stripe", nullable=True
    )
    pdf = Column(String, comment="The link to download the PDF of the credit note")
    reason = Column(
        String,
        comment="Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`",
        nullable=True,
    )
    refund = Column(
        refund,
        comment="[[FK(refund)]] Refund related to this credit note",
        nullable=True,
    )
    status = Column(
        String,
        comment="Status of this credit note, one of `issued` or `void`. Learn more about [voiding credit notes](https://stripe.com/docs/billing/invoices/credit-notes#voiding)",
    )
    subtotal = Column(
        Integer,
        comment="The integer amount in %s representing the amount of the credit note, excluding exclusive tax and invoice level discounts",
    )
    subtotal_excluding_tax = Column(
        Integer,
        comment="The integer amount in %s representing the amount of the credit note, excluding all tax and invoice level discounts",
        nullable=True,
    )
    tax_amounts = Column(
        list, comment="The aggregate amounts calculated per tax rate for all line items"
    )
    total = Column(
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, including tax and all discount",
    )
    total_excluding_tax = Column(
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, excluding tax, but including discounts",
        nullable=True,
    )
    type = Column(
        String,
        comment="Type of this credit note, one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid",
    )
    voided_at = Column(
        Integer, comment="The time that the credit note was voided", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Credit_Note(amount={amount!r}, created={created!r}, currency={currency!r}, customer={customer!r}, customer_balance_transaction={customer_balance_transaction!r}, discount_amount={discount_amount!r}, discount_amounts={discount_amounts!r}, id={id!r}, invoice={invoice!r}, lines={lines!r}, livemode={livemode!r}, memo={memo!r}, metadata={metadata!r}, number={number!r}, object={object!r}, out_of_band_amount={out_of_band_amount!r}, pdf={pdf!r}, reason={reason!r}, refund={refund!r}, status={status!r}, subtotal={subtotal!r}, subtotal_excluding_tax={subtotal_excluding_tax!r}, tax_amounts={tax_amounts!r}, total={total!r}, total_excluding_tax={total_excluding_tax!r}, type={type!r}, voided_at={voided_at!r})".format(
            amount=self.amount,
            created=self.created,
            currency=self.currency,
            customer=self.customer,
            customer_balance_transaction=self.customer_balance_transaction,
            discount_amount=self.discount_amount,
            discount_amounts=self.discount_amounts,
            id=self.id,
            invoice=self.invoice,
            lines=self.lines,
            livemode=self.livemode,
            memo=self.memo,
            metadata=self.metadata,
            number=self.number,
            object=self.object,
            out_of_band_amount=self.out_of_band_amount,
            pdf=self.pdf,
            reason=self.reason,
            refund=self.refund,
            status=self.status,
            subtotal=self.subtotal,
            subtotal_excluding_tax=self.subtotal_excluding_tax,
            tax_amounts=self.tax_amounts,
            total=self.total,
            total_excluding_tax=self.total_excluding_tax,
            type=self.type,
            voided_at=self.voided_at,
        )


__all__ = ["credit_note"]
