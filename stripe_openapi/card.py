from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class Card(Base):
    """
    You can store multiple cards on a customer in order to charge the customer

    later. You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card Payments with Sources](https://stripe.com/docs/sources/cards).

    """

    __tablename__ = "card"
    account = Column(
        Account,
        ForeignKey("Account"),
        comment="The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead",
        nullable=True,
    )
    address_city = Column(
        String, comment="City/District/Suburb/Town/Village", nullable=True
    )
    address_country = Column(
        String,
        comment="Billing address country, if provided when creating card",
        nullable=True,
    )
    address_line1 = Column(
        String,
        comment="Address line 1 (Street address/PO Box/Company name)",
        nullable=True,
    )
    address_line1_check = Column(
        String,
        comment="If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    )
    address_line2 = Column(
        String, comment="Address line 2 (Apartment/Suite/Unit/Building)", nullable=True
    )
    address_state = Column(
        String, comment="State/County/Province/Region", nullable=True
    )
    address_zip = Column(String, comment="ZIP or postal code", nullable=True)
    address_zip_check = Column(
        String,
        comment="If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    )
    available_payout_methods = Column(
        ARRAY(String),
        comment="A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout",
        nullable=True,
    )
    brand = Column(
        String,
        comment="Card brand. Can be `American Express`, `Diners Club`, `Discover`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`",
    )
    country = Column(
        String,
        comment="Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected",
        nullable=True,
    )
    currency = Column(
        String,
        comment="Three-letter [ISO code for currency](https://stripe.com/docs/payouts). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency",
        nullable=True,
    )
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead",
        nullable=True,
    )
    cvc_check = Column(
        String,
        comment="If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn't been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge)",
        nullable=True,
    )
    default_for_currency = Column(
        Boolean,
        comment="Whether this card is the default external account for its currency",
        nullable=True,
    )
    description = Column(
        String,
        comment="A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    dynamic_last4 = Column(
        String,
        comment="(For tokenized numbers only.) The last four digits of the device account number",
        nullable=True,
    )
    exp_month = Column(
        Integer, comment="Two-digit number representing the card's expiration month"
    )
    exp_year = Column(
        Integer, comment="Four-digit number representing the card's expiration year"
    )
    fingerprint = Column(
        String,
        comment="Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.\n\n*Starting May 1, 2021, card fingerprint in India for Connect will change to allow two fingerprints for the same card --- one for India and one for the rest of the world.*",
        nullable=True,
    )
    funding = Column(
        String,
        comment="Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    iin = Column(
        String,
        comment="Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    issuer = Column(
        String,
        comment="The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    last4 = Column(String, comment="The last four digits of the card")
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    name = Column(String, comment="Cardholder name", nullable=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    status = Column(
        String,
        comment="For external accounts, possible values are `new` and `errored`. If a transfer fails, the status is set to `errored` and transfers are stopped until account details are updated",
        nullable=True,
    )
    tokenization_method = Column(
        String,
        comment="If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Card(account={account!r}, address_city={address_city!r}, address_country={address_country!r}, address_line1={address_line1!r}, address_line1_check={address_line1_check!r}, address_line2={address_line2!r}, address_state={address_state!r}, address_zip={address_zip!r}, address_zip_check={address_zip_check!r}, available_payout_methods={available_payout_methods!r}, brand={brand!r}, country={country!r}, currency={currency!r}, customer={customer!r}, cvc_check={cvc_check!r}, default_for_currency={default_for_currency!r}, description={description!r}, dynamic_last4={dynamic_last4!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, id={id!r}, iin={iin!r}, issuer={issuer!r}, last4={last4!r}, metadata={metadata!r}, name={name!r}, object={object!r}, status={status!r}, tokenization_method={tokenization_method!r})".format(
            account=self.account,
            address_city=self.address_city,
            address_country=self.address_country,
            address_line1=self.address_line1,
            address_line1_check=self.address_line1_check,
            address_line2=self.address_line2,
            address_state=self.address_state,
            address_zip=self.address_zip,
            address_zip_check=self.address_zip_check,
            available_payout_methods=self.available_payout_methods,
            brand=self.brand,
            country=self.country,
            currency=self.currency,
            customer=self.customer,
            cvc_check=self.cvc_check,
            default_for_currency=self.default_for_currency,
            description=self.description,
            dynamic_last4=self.dynamic_last4,
            exp_month=self.exp_month,
            exp_year=self.exp_year,
            fingerprint=self.fingerprint,
            funding=self.funding,
            id=self.id,
            iin=self.iin,
            issuer=self.issuer,
            last4=self.last4,
            metadata=self.metadata,
            name=self.name,
            object=self.object,
            status=self.status,
            tokenization_method=self.tokenization_method,
        )


__all__ = ["card"]
