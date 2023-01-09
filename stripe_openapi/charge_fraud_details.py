from sqlalchemy import Column, Identity, Integer, String

from . import Base


class ChargeFraudDetails(Base):
    __tablename__ = "charge_fraud_details"
    stripe_report = Column(
        String,
        comment="Assessments from Stripe. If set, the value is `fraudulent`",
        nullable=True,
    )
    user_report = Column(
        String,
        comment="Assessments reported by you. If set, possible values of are `safe` and `fraudulent`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ChargeFraudDetails(stripe_report={stripe_report!r}, user_report={user_report!r}, id={id!r})".format(
            stripe_report=self.stripe_report, user_report=self.user_report, id=self.id
        )


__all__ = ["charge_fraud_details"]
