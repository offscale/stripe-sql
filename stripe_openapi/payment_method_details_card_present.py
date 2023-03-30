from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from . import metadata

PaymentMethodDetailsCardPresent.Json = Table(
    "payment_method_details_card_present.json",
    metadata,
    Column(
        "amount_authorized", Integer, comment="The authorized amount", nullable=True
    ),
    Column(
        "brand",
        String,
        comment="Card brand. Can be `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    ),
    Column(
        "capture_before",
        Integer,
        comment="When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured",
        nullable=True,
    ),
    Column(
        "cardholder_name",
        String,
        comment="The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column(
        "emv_auth_data",
        String,
        comment="Authorization response cryptogram",
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
        nullable=True,
    ),
    Column(
        "generated_card",
        String,
        comment="ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod",
        nullable=True,
    ),
    Column(
        "iin",
        String,
        comment="Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column(
        "incremental_authorization_supported",
        Boolean,
        comment="Whether this [PaymentIntent](https://stripe.com/docs/api/payment_intents) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support)",
    ),
    Column(
        "issuer",
        String,
        comment="The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    ),
    Column("last4", String, comment="The last four digits of the card", nullable=True),
    Column(
        "network",
        String,
        comment="Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    ),
    Column(
        "overcapture_supported",
        Boolean,
        comment="Defines whether the authorized amount can be over-captured or not",
    ),
    Column(
        "read_method",
        String,
        comment="How card details were read in this transaction",
        nullable=True,
    ),
    Column(
        "receipt",
        PaymentMethodDetailsCardPresentReceipt,
        ForeignKey("PaymentMethodDetailsCardPresentReceipt"),
        comment="A collection of fields required to be displayed on receipts. Only required for EMV transactions",
        nullable=True,
    ),
)
__all__ = ["payment_method_details_card_present.json"]
