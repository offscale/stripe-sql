from sqlalchemy import Column, Identity, Integer

from . import Base


class MandateUsBankAccount(Base):
    __tablename__ = "mandate_us_bank_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "MandateUsBankAccount(id={id!r})".format(id=self.id)


__all__ = ["mandate_us_bank_account"]
