from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceTypeIdeal(Base):
    __tablename__ = "source_type_ideal"
    bank = Column(String, nullable=True)
    bic = Column(String, nullable=True)
    iban_last4 = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeIdeal(bank={bank!r}, bic={bic!r}, iban_last4={iban_last4!r}, statement_descriptor={statement_descriptor!r}, id={id!r})".format(
            bank=self.bank,
            bic=self.bic,
            iban_last4=self.iban_last4,
            statement_descriptor=self.statement_descriptor,
            id=self.id,
        )


__all__ = ["source_type_ideal"]
