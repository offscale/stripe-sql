from sqlalchemy import Column, Integer, String


class Issuing_Dispute_Fraudulent_Evidence(Base):
    __tablename__ = "issuing_dispute_fraudulent_evidence"
    additional_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    )
    explanation = Column(
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Dispute_Fraudulent_Evidence(additional_documentation={additional_documentation!r}, explanation={explanation!r}, id={id!r})".format(
            additional_documentation=self.additional_documentation,
            explanation=self.explanation,
            id=self.id,
        )


__all__ = ["issuing_dispute_fraudulent_evidence"]
