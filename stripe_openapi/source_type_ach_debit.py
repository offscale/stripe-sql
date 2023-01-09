from sqlalchemy import Column, String

from . import Base


class SourceTypeAchDebit(Base):
    __tablename__ = "source_type_ach_debit"
    bank_name = Column(String, nullable=True, primary_key=True)
    country = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    routing_number = Column(String, nullable=True)
    type = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeAchDebit(bank_name={bank_name!r}, country={country!r}, fingerprint={fingerprint!r}, last4={last4!r}, routing_number={routing_number!r}, type={type!r})".format(
            bank_name=self.bank_name,
            country=self.country,
            fingerprint=self.fingerprint,
            last4=self.last4,
            routing_number=self.routing_number,
            type=self.type,
        )


__all__ = ["source_type_ach_debit"]
