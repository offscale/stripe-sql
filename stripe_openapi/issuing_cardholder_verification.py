from sqlalchemy import Column, Integer


class Issuing_Cardholder_Verification(Base):
    __tablename__ = "issuing_cardholder_verification"
    document = Column(
        issuing_cardholder_id_document,
        comment="[[FK(issuing_cardholder_id_document)]] An identifying document, either a passport or local ID card",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "Issuing_Cardholder_Verification(document={document!r}, id={id!r})".format(
                document=self.document, id=self.id
            )
        )


__all__ = ["issuing_cardholder_verification"]
