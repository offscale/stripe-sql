from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.customer import Customer

from . import metadata

CardJson = Table(
    "cardjson",
    metadata,
    Column(
        "account",
        Account,
        ForeignKey("Account"),
        comment="The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead",
        nullable=True,
    ),
    Column(
        "address_city",
        String,
        comment="City/District/Suburb/Town/Village",
        nullable=True,
    ),
    Column(
        "address_country",
        String,
        comment="Billing address country, if provided when creating card",
        nullable=True,
    ),
    Column(
        "address_line1",
        String,
        comment="Address line 1 (Street address/PO Box/Company name)",
        nullable=True,
    ),
    Column(
        "address_line1_check",
        String,
        comment="If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    ),
    Column(
        "address_line2",
        String,
        comment="Address line 2 (Apartment/Suite/Unit/Building)",
        nullable=True,
    ),
    Column(
        "address_state", String, comment="State/County/Province/Region", nullable=True
    ),
    Column("address_zip", String, comment="ZIP or postal code", nullable=True),
    Column(
        "address_zip_check",
        String,
        comment="If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    ),
    Column(
        "available_payout_methods",
        ARRAY(String),
        comment="A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout",
        nullable=True,
    ),
    Column(
        "brand",
        String,
        comment="Card brand. Can be `American Express`, `Diners Club`, `Discover`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`",
    ),
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO code for currency](https://stripe.com/docs/payouts). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency",
        nullable=True,
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead",
        nullable=True,
    ),
    Column(
        "cvc_check",
        String,
        comment="If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn't been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge)",
        nullable=True,
    ),
    Column(
        "default_for_currency",
        Boolean,
        comment="Whether this card is the default external account for its currency",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column(
        "dynamic_last4",
        String,
        comment="(For tokenized numbers only.) The last four digits of the device account number",
        nullable=True,
    ),
    Column(
        "exp_month",
        Integer,
        comment="Two-digit number representing the card's expiration month",
    ),
    Column(
        "exp_year",
        Integer,
        comment="Four-digit number representing the card's expiration year",
    ),
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.\n\n*Starting May 1, 2021, card fingerprint in India for Connect will change to allow two fingerprints for the same card --- one for India and one for the rest of the world.*",
        nullable=True,
    ),
    Column(
        "funding",
        String,
        comment="Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "iin",
        String,
        comment="Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column(
        "issuer",
        String,
        comment="The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column("last4", String, comment="The last four digits of the card"),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column("name", String, comment="Cardholder name", nullable=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "status",
        String,
        comment="For external accounts, possible values are `new` and `errored`. If a transfer fails, the status is set to `errored` and transfers are stopped until account details are updated",
        nullable=True,
    ),
    Column(
        "tokenization_method",
        String,
        comment="If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null",
        nullable=True,
    ),
)
__all__ = ["card.json"]
