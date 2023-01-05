from sqlalchemy import Column, Integer


class Payment_Method_Details_Konbini(Base):
    __tablename__ = "payment_method_details_konbini"
    store = Column(
        PaymentMethodDetailsKonbiniStore,
        comment="If the payment succeeded, this contains the details of the convenience store where the payment was completed",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Details_Konbini(store={store!r}, id={id!r})".format(
            store=self.store, id=self.id
        )


__all__ = ["payment_method_details_konbini"]
