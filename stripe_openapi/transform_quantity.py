from sqlalchemy import Column, Integer, String


class Transform_Quantity(Base):
    __tablename__ = "transform_quantity"
    divide_by = Column(Integer, comment="Divide usage by this number")
    round = Column(
        String, comment="After division, either round the result `up` or `down`"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Transform_Quantity(divide_by={divide_by!r}, round={round!r}, id={id!r})".format(
            divide_by=self.divide_by, round=self.round, id=self.id
        )


__all__ = ["transform_quantity"]
