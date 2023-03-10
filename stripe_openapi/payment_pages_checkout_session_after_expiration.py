from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentPagesCheckoutSessionAfterExpiration(Base):
    __tablename__ = "payment_pages_checkout_session_after_expiration"
    recovery = Column(
        Integer,
        ForeignKey("payment_pages_checkout_session_after_expiration_recovery.id"),
        comment="When set, configuration used to recover the Checkout Session on expiry",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionAfterExpiration(recovery={recovery!r}, id={id!r})".format(
            recovery=self.recovery, id=self.id
        )


__all__ = ["payment_pages_checkout_session_after_expiration"]
