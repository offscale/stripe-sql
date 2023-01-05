from sqlalchemy import Boolean, Column, Integer, String


class Token(Base):
    """
    Tokenization is the process Stripe uses to collect sensitive card or bank

    account details, or personally identifiable information (PII), directly from
    your customers in a secure manner. A token representing this information is
    returned to your server to use. You should use our
    [recommended payments integrations](https://stripe.com/docs/payments) to perform this process
    client-side. This ensures that no sensitive card data touches your server,
    and allows your integration to operate in a PCI-compliant way.

    If you cannot use client-side tokenization, you can also create tokens using
    the API with either your publishable or secret API key. Keep in mind that if
    your integration uses this method, you are responsible for any PCI compliance
    that may be required, and you must keep your secret API key safe. Unlike with
    client-side tokenization, your customer's information is not sent directly to
    Stripe, so we cannot determine how it is handled or stored.

    Tokens cannot be stored or used more than once. To store card or bank account
    information for later use, you can create [Customer](https://stripe.com/docs/api#customers)
    objects or [Custom accounts](https://stripe.com/docs/api#external_accounts). Note that
    [Radar](https://stripe.com/docs/radar), our integrated solution for automatic fraud protection,
    performs best with integrations that use client-side tokenization.

    Related guide: [Accept a payment](https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token)

    """

    __tablename__ = "token"
    bank_account = Column(BankAccount, nullable=True)
    card = Column(Card, nullable=True)
    client_ip = Column(
        String,
        comment="IP address of the client that generated the token",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    type = Column(
        String, comment="Type of the token: `account`, `bank_account`, `card`, or `pii`"
    )
    used = Column(
        Boolean,
        comment="Whether this token has already been used (tokens can be used only once)",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Token(bank_account={bank_account!r}, card={card!r}, client_ip={client_ip!r}, created={created!r}, id={id!r}, livemode={livemode!r}, object={object!r}, type={type!r}, used={used!r})".format(
            bank_account=self.bank_account,
            card=self.card,
            client_ip=self.client_ip,
            created=self.created,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            type=self.type,
            used=self.used,
        )


__all__ = ["token"]
