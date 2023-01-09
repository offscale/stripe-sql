from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class CouponAppliesTo(Base):
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
        return "CouponAppliesTo(products={products!r}, id={id!r})".format(
            products=self.products, id=self.id
        )


__all__ = ["coupon_applies_to"]
