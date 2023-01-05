from sqlalchemy import Column, Integer, String


class Payment_Method_Details_Konbini_Store(Base):
    __tablename__ = "payment_method_details_konbini_store"
    chain = Column(
        String,
        comment="The name of the convenience store chain where the payment was completed",
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
            "Payment_Method_Details_Konbini_Store(chain={chain!r}, id={id!r})".format(
                chain=self.chain, id=self.id
            )
        )


__all__ = ["payment_method_details_konbini_store"]
