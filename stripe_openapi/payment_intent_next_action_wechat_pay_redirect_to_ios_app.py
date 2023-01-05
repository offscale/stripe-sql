from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Wechat_Pay_Redirect_To_Ios_App(Base):
    __tablename__ = "payment_intent_next_action_wechat_pay_redirect_to_ios_app"
    native_url = Column(
        String, comment="An universal link that redirect to WeChat Pay app"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Wechat_Pay_Redirect_To_Ios_App(native_url={native_url!r}, id={id!r})".format(
            native_url=self.native_url, id=self.id
        )


__all__ = ["payment_intent_next_action_wechat_pay_redirect_to_ios_app"]
