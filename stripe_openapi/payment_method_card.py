from sqlalchemy import Column, Integer, String


class Payment_Method_Card(Base):
    __tablename__ = "payment_method_card"
    brand = Column(
        String,
        comment="Card brand. Can be `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
    )
    checks = Column(
        payment_method_card_checks,
        comment="[[FK(payment_method_card_checks)]] Checks on Card address and CVC if provided",
        nullable=True,
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
    networks = Column(
        networks,
        comment="[[FK(networks)]] Contains information about card networks that can be used to process the payment",
        nullable=True,
    )
    three_d_secure_usage = Column(
        three_d_secure_usage,
        comment="[[FK(three_d_secure_usage)]] Contains details on how this Card maybe be used for 3D Secure authentication",
        nullable=True,
    )
    wallet = Column(
        payment_method_card_wallet,
        comment="[[FK(payment_method_card_wallet)]] If this Card is part of a card wallet, this contains the details of the card wallet",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Card(brand={brand!r}, checks={checks!r}, country={country!r}, description={description!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, iin={iin!r}, issuer={issuer!r}, last4={last4!r}, networks={networks!r}, three_d_secure_usage={three_d_secure_usage!r}, wallet={wallet!r}, id={id!r})".format(
            brand=self.brand,
            checks=self.checks,
            country=self.country,
            description=self.description,
            exp_month=self.exp_month,
            exp_year=self.exp_year,
            fingerprint=self.fingerprint,
            funding=self.funding,
            iin=self.iin,
            issuer=self.issuer,
            last4=self.last4,
            networks=self.networks,
            three_d_secure_usage=self.three_d_secure_usage,
            wallet=self.wallet,
            id=self.id,
        )


__all__ = ["payment_method_card"]
