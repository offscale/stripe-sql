from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Alipay_Handle_Redirect(Base):
    __tablename__ = "payment_intent_next_action_alipay_handle_redirect"
    native_data = Column(
        String,
        comment="The native data to be used with Alipay SDK you must redirect your customer to in order to authenticate the payment in an Android App",
        nullable=True,
    )
    native_url = Column(
        String,
        comment="The native URL you must redirect your customer to in order to authenticate the payment in an iOS App",
        nullable=True,
    )
    return_url = Column(
        String,
        comment="If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion",
        nullable=True,
    )
    url = Column(
        String,
        comment="The URL you must redirect your customer to in order to authenticate the payment",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Alipay_Handle_Redirect(native_data={native_data!r}, native_url={native_url!r}, return_url={return_url!r}, url={url!r}, id={id!r})".format(
            native_data=self.native_data,
            native_url=self.native_url,
            return_url=self.return_url,
            url=self.url,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_alipay_handle_redirect"]
