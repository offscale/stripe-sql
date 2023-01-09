from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceTypeP24(Base):
    __tablename__ = "source_type_p24"
    reference = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeP24(reference={reference!r}, id={id!r})".format(
            reference=self.reference, id=self.id
        )


__all__ = ["source_type_p24"]
