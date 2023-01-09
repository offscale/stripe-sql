from sqlalchemy import Column, Identity, Integer

from stripe_openapi.setup_attempt import SetupAttempt

from . import Base


class SepaDebitGeneratedFrom(Base):
    __tablename__ = "sepa_debit_generated_from"
    charge = Column(
        Charge,
        comment="[[FK(Charge)]] The ID of the Charge that generated this PaymentMethod, if any",
        nullable=True,
    )
    setup_attempt = Column(
        SetupAttempt,
        comment="[[FK(SetupAttempt)]] The ID of the SetupAttempt that generated this PaymentMethod, if any",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SepaDebitGeneratedFrom(charge={charge!r}, setup_attempt={setup_attempt!r}, id={id!r})".format(
            charge=self.charge, setup_attempt=self.setup_attempt, id=self.id
        )


__all__ = ["sepa_debit_generated_from"]
