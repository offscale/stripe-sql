from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentIntentNextActionKonbiniStores(Base):
    __tablename__ = "payment_intent_next_action_konbini_stores"
    familymart = Column(
        Integer,
        ForeignKey("payment_intent_next_action_konbini_familymart.id"),
        comment="FamilyMart instruction details",
        nullable=True,
    )
    lawson = Column(
        Integer,
        ForeignKey("payment_intent_next_action_konbini_lawson.id"),
        comment="Lawson instruction details",
        nullable=True,
    )
    ministop = Column(
        Integer,
        ForeignKey("payment_intent_next_action_konbini_ministop.id"),
        comment="Ministop instruction details",
        nullable=True,
    )
    seicomart = Column(
        Integer,
        ForeignKey("payment_intent_next_action_konbini_seicomart.id"),
        comment="Seicomart instruction details",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionKonbiniStores(familymart={familymart!r}, lawson={lawson!r}, ministop={ministop!r}, seicomart={seicomart!r}, id={id!r})".format(
            familymart=self.familymart,
            lawson=self.lawson,
            ministop=self.ministop,
            seicomart=self.seicomart,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_konbini_stores"]
