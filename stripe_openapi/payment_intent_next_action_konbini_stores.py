from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_intent_next_action_konbini_familymart import (
    PaymentIntentNextActionKonbiniFamilymart,
)
from stripe_openapi.payment_intent_next_action_konbini_lawson import (
    PaymentIntentNextActionKonbiniLawson,
)
from stripe_openapi.payment_intent_next_action_konbini_ministop import (
    PaymentIntentNextActionKonbiniMinistop,
)
from stripe_openapi.payment_intent_next_action_konbini_seicomart import (
    PaymentIntentNextActionKonbiniSeicomart,
)

from . import Base


class PaymentIntentNextActionKonbiniStores(Base):
    __tablename__ = "payment_intent_next_action_konbini_stores"
    familymart = Column(
        PaymentIntentNextActionKonbiniFamilymart,
        comment="[[FK(PaymentIntentNextActionKonbiniFamilymart)]] FamilyMart instruction details",
        nullable=True,
    )
    lawson = Column(
        PaymentIntentNextActionKonbiniLawson,
        comment="[[FK(PaymentIntentNextActionKonbiniLawson)]] Lawson instruction details",
        nullable=True,
    )
    ministop = Column(
        PaymentIntentNextActionKonbiniMinistop,
        comment="[[FK(PaymentIntentNextActionKonbiniMinistop)]] Ministop instruction details",
        nullable=True,
    )
    seicomart = Column(
        PaymentIntentNextActionKonbiniSeicomart,
        comment="[[FK(PaymentIntentNextActionKonbiniSeicomart)]] Seicomart instruction details",
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
