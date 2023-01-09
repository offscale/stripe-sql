from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentFlowsPrivatePaymentMethodsAlipay(Base):
    __tablename__ = "payment_flows_private_payment_methods_alipay"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentFlowsPrivatePaymentMethodsAlipay(id={id!r})".format(id=self.id)


__all__ = ["payment_flows_private_payment_methods_alipay"]
