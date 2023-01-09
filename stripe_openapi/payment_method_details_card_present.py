from sqlalchemy import Boolean, Column, Integer, String

from stripe_openapi.payment_method_details_card_present_receipt import (
    PaymentMethodDetailsCardPresentReceipt,
)

from . import Base


class PaymentMethodDetailsCardPresent(Base):
    __tablename__ = "payment_method_details_card_present"
    amount_authorized = Column(Integer, comment="The authorized amount", nullable=True)
    brand = Column(
        String,
        comment="Card brand. Can be `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    )
    capture_before = Column(
        Integer,
        comment="When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured",
        nullable=True,
    )
    cardholder_name = Column(
        String,
        comment="The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay",
        nullable=True,
        primary_key=True,
    )
    country = Column(
        String,
        comment="Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected",
        nullable=True,
    )
    description = Column(
        String,
        comment="A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    emv_auth_data = Column(
        String, comment="Authorization response cryptogram", nullable=True
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
        nullable=True,
    )
    generated_card = Column(
        String,
        comment="ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod",
        nullable=True,
    )
    iin = Column(
        String,
        comment="Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    incremental_authorization_supported = Column(
        Boolean,
        comment="Whether this [PaymentIntent](https://stripe.com/docs/api/payment_intents) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support)",
    )
    issuer = Column(
        String,
        comment="The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    last4 = Column(String, comment="The last four digits of the card", nullable=True)
    network = Column(
        String,
        comment="Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    )
    overcapture_supported = Column(
        Boolean,
        comment="Defines whether the authorized amount can be over-captured or not",
    )
    read_method = Column(
        String, comment="How card details were read in this transaction", nullable=True
    )
    receipt = Column(
        PaymentMethodDetailsCardPresentReceipt,
        comment="[[FK(PaymentMethodDetailsCardPresentReceipt)]] A collection of fields required to be displayed on receipts. Only required for EMV transactions",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsCardPresent(amount_authorized={amount_authorized!r}, brand={brand!r}, capture_before={capture_before!r}, cardholder_name={cardholder_name!r}, country={country!r}, description={description!r}, emv_auth_data={emv_auth_data!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, generated_card={generated_card!r}, iin={iin!r}, incremental_authorization_supported={incremental_authorization_supported!r}, issuer={issuer!r}, last4={last4!r}, network={network!r}, overcapture_supported={overcapture_supported!r}, read_method={read_method!r}, receipt={receipt!r})".format(
            amount_authorized=self.amount_authorized,
            brand=self.brand,
            capture_before=self.capture_before,
            cardholder_name=self.cardholder_name,
            country=self.country,
            description=self.description,
            emv_auth_data=self.emv_auth_data,
            exp_month=self.exp_month,
            exp_year=self.exp_year,
            fingerprint=self.fingerprint,
            funding=self.funding,
            generated_card=self.generated_card,
            iin=self.iin,
            incremental_authorization_supported=self.incremental_authorization_supported,
            issuer=self.issuer,
            last4=self.last4,
            network=self.network,
            overcapture_supported=self.overcapture_supported,
            read_method=self.read_method,
            receipt=self.receipt,
        )


__all__ = ["payment_method_details_card_present"]
