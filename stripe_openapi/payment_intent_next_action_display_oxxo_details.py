from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Display_Oxxo_Details(Base):
    __tablename__ = "payment_intent_next_action_display_oxxo_details"
    expires_after = Column(
        Integer,
        comment="The timestamp after which the OXXO voucher expires",
        nullable=True,
    )
    hosted_voucher_url = Column(
        String,
        comment="The URL for the hosted OXXO voucher page, which allows customers to view and print an OXXO voucher",
        nullable=True,
    )
    number = Column(String, comment="OXXO reference number", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Display_Oxxo_Details(expires_after={expires_after!r}, hosted_voucher_url={hosted_voucher_url!r}, number={number!r}, id={id!r})".format(
            expires_after=self.expires_after,
            hosted_voucher_url=self.hosted_voucher_url,
            number=self.number,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_display_oxxo_details"]
