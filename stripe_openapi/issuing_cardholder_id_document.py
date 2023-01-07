from sqlalchemy import Column, Integer


class Issuing_Cardholder_Id_Document(Base):
    __tablename__ = "issuing_cardholder_id_document"
    back = Column(
        file,
        comment="[[FK(file)]] The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    )
    front = Column(
        file,
        comment="[[FK(file)]] The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Cardholder_Id_Document(back={back!r}, front={front!r}, id={id!r})".format(
            back=self.back, front=self.front, id=self.id
        )


__all__ = ["issuing_cardholder_id_document"]
