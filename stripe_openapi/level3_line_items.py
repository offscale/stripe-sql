from sqlalchemy import Column, Identity, Integer, String

from . import Base


class Level3LineItems(Base):
    __tablename__ = "level3_line_items"
    discount_amount = Column(Integer, nullable=True)
    product_code = Column(String)
    product_description = Column(String)
    quantity = Column(Integer, nullable=True)
    tax_amount = Column(Integer, nullable=True)
    unit_cost = Column(Integer, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Level3LineItems(discount_amount={discount_amount!r}, product_code={product_code!r}, product_description={product_description!r}, quantity={quantity!r}, tax_amount={tax_amount!r}, unit_cost={unit_cost!r}, id={id!r})".format(
            discount_amount=self.discount_amount,
            product_code=self.product_code,
            product_description=self.product_description,
            quantity=self.quantity,
            tax_amount=self.tax_amount,
            unit_cost=self.unit_cost,
            id=self.id,
        )


__all__ = ["level3_line_items"]
