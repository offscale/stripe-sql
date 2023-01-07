from sqlalchemy import Boolean, Column, Integer, String


class Payment_Method_Details_Card(Base):
    __tablename__ = "payment_method_details_card"
    brand = Column(
        String,
        comment="Card brand. Can be `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    )
    checks = Column(
        payment_method_details_card_checks,
        comment="[[FK(payment_method_details_card_checks)]] Check results by Card networks on Card address and CVC at time of payment",
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
        nullable=True,
    )
    iin = Column(
        String,
        comment="Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    installments = Column(
        payment_method_details_card_installments,
        comment="[[FK(payment_method_details_card_installments)]] Installment details for this payment (Mexico only).\n\nFor more information, see the [installments integration guide](https://stripe.com/docs/payments/installments)",
        nullable=True,
    )
    issuer = Column(
        String,
        comment="The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)",
        nullable=True,
    )
    last4 = Column(String, comment="The last four digits of the card", nullable=True)
    mandate = Column(
        String,
        comment="ID of the mandate used to make this payment or created by it",
        nullable=True,
    )
    moto = Column(
        Boolean,
        comment="True if this payment was marked as MOTO and out of scope for SCA",
        nullable=True,
    )
    network = Column(
        String,
        comment="Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `interac`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`",
        nullable=True,
    )
    three_d_secure = Column(
        three_d_secure_details,
        comment="[[FK(three_d_secure_details)]] Populated if this transaction used 3D Secure authentication",
        nullable=True,
    )
    wallet = Column(
        payment_method_details_card_wallet,
        comment="[[FK(payment_method_details_card_wallet)]] If this Card is part of a card wallet, this contains the details of the card wallet",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Card(brand={brand!r}, checks={checks!r}, country={country!r}, description={description!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, iin={iin!r}, installments={installments!r}, issuer={issuer!r}, last4={last4!r}, mandate={mandate!r}, moto={moto!r}, network={network!r}, three_d_secure={three_d_secure!r}, wallet={wallet!r}, id={id!r})".format(
            brand=self.brand,
            checks=self.checks,
            country=self.country,
            description=self.description,
            exp_month=self.exp_month,
            exp_year=self.exp_year,
            fingerprint=self.fingerprint,
            funding=self.funding,
            iin=self.iin,
            installments=self.installments,
            issuer=self.issuer,
            last4=self.last4,
            mandate=self.mandate,
            moto=self.moto,
            network=self.network,
            three_d_secure=self.three_d_secure,
            wallet=self.wallet,
            id=self.id,
        )


__all__ = ["payment_method_details_card"]
