from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceTypeAuBecsDebit(Base):
    __tablename__ = "source_type_au_becs_debit"
    bsb_number = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeAuBecsDebit(bsb_number={bsb_number!r}, fingerprint={fingerprint!r}, last4={last4!r}, id={id!r})".format(
            bsb_number=self.bsb_number,
            fingerprint=self.fingerprint,
            last4=self.last4,
            id=self.id,
        )


__all__ = ["source_type_au_becs_debit"]
