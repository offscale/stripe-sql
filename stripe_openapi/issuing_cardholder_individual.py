from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class IssuingCardholderIndividual(Base):
    __tablename__ = "issuing_cardholder_individual"
    card_issuing = Column(
        Integer, ForeignKey("issuing_cardholder_card_issuing.id"), nullable=True
    )
    dob = Column(
        Integer,
        ForeignKey("issuing_cardholder_individual_dob.id"),
        comment="The date of birth of this cardholder",
        nullable=True,
    )
    first_name = Column(String, comment="The first name of this cardholder")
    last_name = Column(String, comment="The last name of this cardholder")
    verification = Column(
        Integer,
        ForeignKey("issuing_cardholder_verification.id"),
        comment="Government-issued ID document for this cardholder",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderIndividual(card_issuing={card_issuing!r}, dob={dob!r}, first_name={first_name!r}, last_name={last_name!r}, verification={verification!r}, id={id!r})".format(
            card_issuing=self.card_issuing,
            dob=self.dob,
            first_name=self.first_name,
            last_name=self.last_name,
            verification=self.verification,
            id=self.id,
        )


__all__ = ["issuing_cardholder_individual"]
