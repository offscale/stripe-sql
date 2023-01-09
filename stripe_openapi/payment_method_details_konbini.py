from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_method_details_konbini_store import (
    PaymentMethodDetailsKonbiniStore,
)

from . import Base


class PaymentMethodDetailsKonbini(Base):
    __tablename__ = "payment_method_details_konbini"
    store = Column(
        PaymentMethodDetailsKonbiniStore,
        comment="[[FK(PaymentMethodDetailsKonbiniStore)]] If the payment succeeded, this contains the details of the convenience store where the payment was completed",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsKonbini(store={store!r}, id={id!r})".format(
            store=self.store, id=self.id
        )


__all__ = ["payment_method_details_konbini"]
