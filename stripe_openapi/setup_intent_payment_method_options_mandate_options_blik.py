from sqlalchemy import Column, Integer, String


class Setup_Intent_Payment_Method_Options_Mandate_Options_Blik(Base):
    __tablename__ = "setup_intent_payment_method_options_mandate_options_blik"
    expires_after = Column(
        Integer, comment="Date at which the mandate expires", nullable=True
    )
    off_session = Column(MandateOptionsOffSessionDetailsBlik, nullable=True)
    type = Column(String, comment="Type of the mandate", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Intent_Payment_Method_Options_Mandate_Options_Blik(expires_after={expires_after!r}, off_session={off_session!r}, type={type!r}, id={id!r})".format(
            expires_after=self.expires_after,
            off_session=self.off_session,
            type=self.type,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options_mandate_options_blik"]
