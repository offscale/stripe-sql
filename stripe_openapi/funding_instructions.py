from sqlalchemy import Boolean, Column, Integer, String


class Funding_Instructions(Base):
    """
    Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) that is

    automatically applied to future invoices and payments using the `customer_balance` payment method.
    Customers can fund this balance by initiating a bank transfer to any account in the
    `financial_addresses` field.
    Related guide: [Customer Balance - Funding Instructions](https://stripe.com/docs/payments/customer-balance/funding-instructions) to learn more

    """

    __tablename__ = "funding_instructions"
    bank_transfer = Column(
        funding_instructions_bank_transfer,
        ForeignKey("funding_instructions_bank_transfer"),
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    funding_type = Column(
        String, comment="The `funding_type` of the returned instructions"
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Funding_Instructions(bank_transfer={bank_transfer!r}, currency={currency!r}, funding_type={funding_type!r}, livemode={livemode!r}, object={object!r}, id={id!r})".format(
            bank_transfer=self.bank_transfer,
            currency=self.currency,
            funding_type=self.funding_type,
            livemode=self.livemode,
            object=self.object,
            id=self.id,
        )


__all__ = ["funding_instructions"]
