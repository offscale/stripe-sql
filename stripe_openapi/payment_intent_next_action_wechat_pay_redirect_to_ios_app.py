from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentNextActionWechatPayRedirectToIosApp(Base):
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
        return "PaymentIntentNextActionWechatPayRedirectToIosApp(native_url={native_url!r}, id={id!r})".format(
            native_url=self.native_url, id=self.id
        )


__all__ = ["payment_intent_next_action_wechat_pay_redirect_to_ios_app"]
