from sqlalchemy import Column, Identity, Integer

from . import Base


class MandateMultiUse(Base):
    __tablename__ = "mandate_multi_use"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "MandateMultiUse(id={id!r})".format(id=self.id)


__all__ = ["mandate_multi_use"]
