from sqlalchemy import Boolean, Column, Identity, Integer, String

from . import Base


class IssuingCardApplePay(Base):
    __tablename__ = "issuing_card_apple_pay"
    eligible = Column(Boolean, comment="Apple Pay Eligibility")
    ineligible_reason = Column(
        String, comment="Reason the card is ineligible for Apple Pay", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardApplePay(eligible={eligible!r}, ineligible_reason={ineligible_reason!r}, id={id!r})".format(
            eligible=self.eligible, ineligible_reason=self.ineligible_reason, id=self.id
        )


__all__ = ["issuing_card_apple_pay"]
