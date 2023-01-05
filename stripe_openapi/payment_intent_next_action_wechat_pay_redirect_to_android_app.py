from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Wechat_Pay_Redirect_To_Android_App(Base):
    __tablename__ = "payment_intent_next_action_wechat_pay_redirect_to_android_app"
    app_id = Column(
        String, comment="app_id is the APP ID registered on WeChat open platform"
    )
    nonce_str = Column(String, comment="nonce_str is a random string")
    package = Column(String, comment="package is static value")
    partner_id = Column(String, comment="an unique merchant ID assigned by WeChat Pay")
    prepay_id = Column(String, comment="an unique trading ID assigned by WeChat Pay")
    sign = Column(String, comment="A signature")
    timestamp = Column(String, comment="Specifies the current time in epoch format")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Wechat_Pay_Redirect_To_Android_App(app_id={app_id!r}, nonce_str={nonce_str!r}, package={package!r}, partner_id={partner_id!r}, prepay_id={prepay_id!r}, sign={sign!r}, timestamp={timestamp!r}, id={id!r})".format(
            app_id=self.app_id,
            nonce_str=self.nonce_str,
            package=self.package,
            partner_id=self.partner_id,
            prepay_id=self.prepay_id,
            sign=self.sign,
            timestamp=self.timestamp,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_wechat_pay_redirect_to_android_app"]
