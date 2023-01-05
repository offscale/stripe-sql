from sqlalchemy import Column, Integer


class Mandate_Us_Bank_Account(Base):
    __tablename__ = "mandate_us_bank_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Mandate_Us_Bank_Account(id={id!r})".format(id=self.id)


__all__ = ["mandate_us_bank_account"]
