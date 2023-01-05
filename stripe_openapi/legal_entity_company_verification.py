from sqlalchemy import Column, Integer


class Legal_Entity_Company_Verification(Base):
    __tablename__ = "legal_entity_company_verification"
    document = Column(LegalEntityCompanyVerificationDocument)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Legal_Entity_Company_Verification(document={document!r}, id={id!r})".format(
            document=self.document, id=self.id
        )


__all__ = ["legal_entity_company_verification"]
