from sqlalchemy import Column, String

from . import Base


class SourceTypeSofort(Base):
    __tablename__ = "source_type_sofort"
    bank_code = Column(String, nullable=True)
    bank_name = Column(String, nullable=True, primary_key=True)
    bic = Column(String, nullable=True)
    country = Column(String, nullable=True)
    iban_last4 = Column(String, nullable=True)
    preferred_language = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeSofort(bank_code={bank_code!r}, bank_name={bank_name!r}, bic={bic!r}, country={country!r}, iban_last4={iban_last4!r}, preferred_language={preferred_language!r}, statement_descriptor={statement_descriptor!r})".format(
            bank_code=self.bank_code,
            bank_name=self.bank_name,
            bic=self.bic,
            country=self.country,
            iban_last4=self.iban_last4,
            preferred_language=self.preferred_language,
            statement_descriptor=self.statement_descriptor,
        )


__all__ = ["source_type_sofort"]
