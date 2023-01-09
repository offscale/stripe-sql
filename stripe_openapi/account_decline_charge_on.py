from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class AccountDeclineChargeOn(Base):
    __tablename__ = "account_decline_charge_on"
    avs_failure = Column(
        Boolean,
        comment="Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification",
    )
    cvc_failure = Column(
        Boolean,
        comment="Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountDeclineChargeOn(avs_failure={avs_failure!r}, cvc_failure={cvc_failure!r}, id={id!r})".format(
            avs_failure=self.avs_failure, cvc_failure=self.cvc_failure, id=self.id
        )


__all__ = ["account_decline_charge_on"]
