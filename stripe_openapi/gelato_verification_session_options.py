from sqlalchemy import Column, ForeignKey

from stripe_openapi.gelato_session_id_number_options import GelatoSessionIdNumberOptions

from . import Base


class GelatoVerificationSessionOptions(Base):
    __tablename__ = "gelato_verification_session_options"
    document = Column(
        Boolean,
        ForeignKey("gelato_session_document_options.require_id_number"),
        nullable=True,
    )
    id_number = Column(
        GelatoSessionIdNumberOptions,
        comment="[FK(GelatoSessionIdNumberOptions)]",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoVerificationSessionOptions(document={document!r}, id_number={id_number!r})".format(
            document=self.document, id_number=self.id_number
        )


__all__ = ["gelato_verification_session_options"]
