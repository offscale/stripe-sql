from sqlalchemy import Column, Identity, Integer

from stripe_openapi.three_d_secure_details import ThreeDSecureDetails

from . import Base


class SetupAttemptPaymentMethodDetailsCard(Base):
    __tablename__ = "setup_attempt_payment_method_details_card"
    three_d_secure = Column(
        ThreeDSecureDetails,
        comment="[[FK(ThreeDSecureDetails)]] Populated if this authorization used 3D Secure authentication",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupAttemptPaymentMethodDetailsCard(three_d_secure={three_d_secure!r}, id={id!r})".format(
            three_d_secure=self.three_d_secure, id=self.id
        )


__all__ = ["setup_attempt_payment_method_details_card"]
