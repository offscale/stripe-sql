from sqlalchemy import Column, Integer


class Payment_Intent_Next_Action_Konbini_Stores(Base):
    __tablename__ = "payment_intent_next_action_konbini_stores"
    familymart = Column(
        payment_intent_next_action_konbini_familymart,
        comment="[[FK(payment_intent_next_action_konbini_familymart)]] FamilyMart instruction details",
        nullable=True,
    )
    lawson = Column(
        payment_intent_next_action_konbini_lawson,
        comment="[[FK(payment_intent_next_action_konbini_lawson)]] Lawson instruction details",
        nullable=True,
    )
    ministop = Column(
        payment_intent_next_action_konbini_ministop,
        comment="[[FK(payment_intent_next_action_konbini_ministop)]] Ministop instruction details",
        nullable=True,
    )
    seicomart = Column(
        payment_intent_next_action_konbini_seicomart,
        comment="[[FK(payment_intent_next_action_konbini_seicomart)]] Seicomart instruction details",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Konbini_Stores(familymart={familymart!r}, lawson={lawson!r}, ministop={ministop!r}, seicomart={seicomart!r}, id={id!r})".format(
            familymart=self.familymart,
            lawson=self.lawson,
            ministop=self.ministop,
            seicomart=self.seicomart,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_konbini_stores"]
