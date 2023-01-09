from sqlalchemy import Column, Identity, Integer

from . import Base


class GelatoSessionIdNumberOptions(Base):
    __tablename__ = "gelato_session_id_number_options"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoSessionIdNumberOptions(id={id!r})".format(id=self.id)


__all__ = ["gelato_session_id_number_options"]
