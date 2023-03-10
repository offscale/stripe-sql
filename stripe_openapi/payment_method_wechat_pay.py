from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentMethodWechatPay(Base):
    __tablename__ = "payment_method_wechat_pay"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodWechatPay(id={id!r})".format(id=self.id)


__all__ = ["payment_method_wechat_pay"]
