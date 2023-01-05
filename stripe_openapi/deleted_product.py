from sqlalchemy import Boolean, Column, String


class Deleted_Product(Base):
    __tablename__ = "deleted_product"
    deleted = Column(Boolean, comment="Always true for a deleted object")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "Deleted_Product(deleted={deleted!r}, id={id!r}, object={object!r})".format(
                deleted=self.deleted, id=self.id, object=self.object
            )
        )


__all__ = ["deleted_product"]
