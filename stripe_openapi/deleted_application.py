from sqlalchemy import Boolean, Column, String


class Deleted_Application(Base):
    __tablename__ = "deleted_application"
    deleted = Column(Boolean, comment="Always true for a deleted object")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    name = Column(String, comment="The name of the application", nullable=True)
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
        return "Deleted_Application(deleted={deleted!r}, id={id!r}, name={name!r}, object={object!r})".format(
            deleted=self.deleted, id=self.id, name=self.name, object=self.object
        )


__all__ = ["deleted_application"]
