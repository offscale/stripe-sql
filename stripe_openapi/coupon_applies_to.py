from sqlalchemy import Column, Integer


class Coupon_Applies_To(Base):
    __tablename__ = "coupon_applies_to"
    products = Column(
        ARRAY(String), comment="A list of product IDs this coupon applies to"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Coupon_Applies_To(products={products!r}, id={id!r})".format(
            products=self.products, id=self.id
        )


__all__ = ["coupon_applies_to"]
