from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class LegalEntityCompanyVerification(Base):
    __tablename__ = "legal_entity_company_verification"
    document = Column(
        Integer, ForeignKey("legal_entity_company_verification_document.id")
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "LegalEntityCompanyVerification(document={document!r}, id={id!r})".format(
                document=self.document, id=self.id
            )
        )


__all__ = ["legal_entity_company_verification"]
