from sqlalchemy import Column, Integer


class Offline_Acceptance(Base):
    __tablename__ = "offline_acceptance"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Offline_Acceptance(id={id!r})".format(id=self.id)


__all__ = ["offline_acceptance"]
