from sqlalchemy import Column, String


class Issuing_Card_Wallets(Base):
    __tablename__ = "issuing_card_wallets"
    apple_pay = Column(IssuingCardApplePay)
    google_pay = Column(IssuingCardGooglePay)
    primary_account_identifier = Column(
        String,
        comment="Unique identifier for a card used with digital wallets",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Card_Wallets(apple_pay={apple_pay!r}, google_pay={google_pay!r}, primary_account_identifier={primary_account_identifier!r})".format(
            apple_pay=self.apple_pay,
            google_pay=self.google_pay,
            primary_account_identifier=self.primary_account_identifier,
        )


__all__ = ["issuing_card_wallets"]
