from sqlalchemy import Column, Identity, Integer

from . import Base


class CheckoutPixPaymentMethodOptions(Base):
    __tablename__ = "checkout_pix_payment_method_options"
    expires_after_seconds = Column(
        Integer,
        comment="The number of seconds after which Pix payment will expire",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CheckoutPixPaymentMethodOptions(expires_after_seconds={expires_after_seconds!r}, id={id!r})".format(
            expires_after_seconds=self.expires_after_seconds, id=self.id
        )


__all__ = ["checkout_pix_payment_method_options"]
