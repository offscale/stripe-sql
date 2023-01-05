from sqlalchemy import Column, Integer, String


class Portal_Subscription_Update_Product(Base):
    __tablename__ = "portal_subscription_update_product"
    prices = Column(
        ARRAY(String),
        comment="The list of price IDs which, when subscribed to, a subscription can be updated",
    )
    product = Column(String, comment="The product ID")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Portal_Subscription_Update_Product(prices={prices!r}, product={product!r}, id={id!r})".format(
            prices=self.prices, product=self.product, id=self.id
        )


__all__ = ["portal_subscription_update_product"]
