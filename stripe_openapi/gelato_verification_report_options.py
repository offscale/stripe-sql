from sqlalchemy import Column


class Gelato_Verification_Report_Options(Base):
    __tablename__ = "gelato_verification_report_options"
    document = Column(
        gelato_report_document_options,
        ForeignKey("gelato_report_document_options"),
        nullable=True,
    )
    id_number = Column(
        gelato_report_id_number_options,
        comment="[FK(gelato_report_id_number_options)]",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Gelato_Verification_Report_Options(document={document!r}, id_number={id_number!r})".format(
            document=self.document, id_number=self.id_number
        )


__all__ = ["gelato_verification_report_options"]
