from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class SetupIntentPaymentMethodOptionsMandateOptionsBlik(Base):
    __tablename__ = "setup_intent_payment_method_options_mandate_options_blik"
    expires_after = Column(
        Integer, comment="Date at which the mandate expires", nullable=True
    )
    off_session = Column(
        Integer,
        ForeignKey("mandate_options_off_session_details_blik.id"),
        nullable=True,
    )
    type = Column(String, comment="Type of the mandate", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentPaymentMethodOptionsMandateOptionsBlik(expires_after={expires_after!r}, off_session={off_session!r}, type={type!r}, id={id!r})".format(
            expires_after=self.expires_after,
            off_session=self.off_session,
            type=self.type,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options_mandate_options_blik"]
