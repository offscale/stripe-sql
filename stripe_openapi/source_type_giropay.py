from sqlalchemy import Column, String

from . import Base


class SourceTypeGiropay(Base):
    __tablename__ = "source_type_giropay"
    bank_code = Column(String, nullable=True)
    bank_name = Column(String, nullable=True, primary_key=True)
    bic = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeGiropay(bank_code={bank_code!r}, bank_name={bank_name!r}, bic={bic!r}, statement_descriptor={statement_descriptor!r})".format(
            bank_code=self.bank_code,
            bank_name=self.bank_name,
            bic=self.bic,
            statement_descriptor=self.statement_descriptor,
        )


__all__ = ["source_type_giropay"]
