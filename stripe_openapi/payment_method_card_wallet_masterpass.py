from sqlalchemy import Column, Integer, String


class Payment_Method_Card_Wallet_Masterpass(Base):
    __tablename__ = "payment_method_card_wallet_masterpass"
    billing_address = Column(
        Address,
        comment="Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    email = Column(
        String,
        comment="Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    name = Column(
        String,
        comment="Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    shipping_address = Column(
        Address,
        comment="Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Card_Wallet_Masterpass(billing_address={billing_address!r}, email={email!r}, name={name!r}, shipping_address={shipping_address!r}, id={id!r})".format(
            billing_address=self.billing_address,
            email=self.email,
            name=self.name,
            shipping_address=self.shipping_address,
            id=self.id,
        )


__all__ = ["payment_method_card_wallet_masterpass"]
