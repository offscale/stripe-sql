from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentMethodDetailsCardWalletSamsungPay(Base):
    __tablename__ = "payment_method_details_card_wallet_samsung_pay"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsCardWalletSamsungPay(id={id!r})".format(id=self.id)


__all__ = ["payment_method_details_card_wallet_samsung_pay"]
