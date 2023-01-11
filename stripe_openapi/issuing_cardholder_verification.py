from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class IssuingCardholderVerification(Base):
    __tablename__ = "issuing_cardholder_verification"
    document = Column(
        Integer,
        ForeignKey("issuing_cardholder_id_document.id"),
        comment="An identifying document, either a passport or local ID card",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderVerification(document={document!r}, id={id!r})".format(
            document=self.document, id=self.id
        )


__all__ = ["issuing_cardholder_verification"]
