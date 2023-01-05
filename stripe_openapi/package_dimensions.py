from sqlalchemy import Column, Float, Integer


class Package_Dimensions(Base):
    __tablename__ = "package_dimensions"
    height = Column(Float, comment="Height, in inches")
    length = Column(Float, comment="Length, in inches")
    weight = Column(Float, comment="Weight, in ounces")
    width = Column(Float, comment="Width, in inches")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Package_Dimensions(height={height!r}, length={length!r}, weight={weight!r}, width={width!r}, id={id!r})".format(
            height=self.height,
            length=self.length,
            weight=self.weight,
            width=self.width,
            id=self.id,
        )


__all__ = ["package_dimensions"]
