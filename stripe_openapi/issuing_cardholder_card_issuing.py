from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class IssuingCardholderCardIssuing(Base):
    __tablename__ = "issuing_cardholder_card_issuing"
    user_terms_acceptance = Column(
        Integer,
        ForeignKey("issuing_cardholder_user_terms_acceptance.id"),
        comment="Information about cardholder acceptance of [Authorized User Terms](https://stripe.com/docs/issuing/cards)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderCardIssuing(user_terms_acceptance={user_terms_acceptance!r}, id={id!r})".format(
            user_terms_acceptance=self.user_terms_acceptance, id=self.id
        )


__all__ = ["issuing_cardholder_card_issuing"]
