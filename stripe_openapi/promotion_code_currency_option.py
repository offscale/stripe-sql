from sqlalchemy import Column, Integer


class Promotion_Code_Currency_Option(Base):
    __tablename__ = "promotion_code_currency_option"
    minimum_amount = Column(
        Integer,
        comment="Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work)",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Promotion_Code_Currency_Option(minimum_amount={minimum_amount!r}, id={id!r})".format(
            minimum_amount=self.minimum_amount, id=self.id
        )


__all__ = ["promotion_code_currency_option"]
