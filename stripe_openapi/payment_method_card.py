from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.networks import Networks

from . import metadata

PaymentMethodCardJson = Table(
    "payment_method_cardjson",
    metadata,
    Column(
        "brand",
        String,
        comment="Card brand. Can be `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
    ),
    Column(
        "checks",
        PaymentMethodCardChecks,
        ForeignKey("PaymentMethodCardChecks"),
        comment="Checks on Card address and CVC if provided",
        nullable=True,
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
        "networks",
        Networks,
        ForeignKey("Networks"),
        comment="Contains information about card networks that can be used to process the payment",
        nullable=True,
    ),
    Column(
        "three_d_secure_usage",
        ThreeDSecureUsage,
        ForeignKey("ThreeDSecureUsage"),
        comment="Contains details on how this Card may be used for 3D Secure authentication",
        nullable=True,
    ),
    Column(
        "wallet",
        PaymentMethodCardWallet,
        ForeignKey("PaymentMethodCardWallet"),
        comment="If this Card is part of a card wallet, this contains the details of the card wallet",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card.json"]
