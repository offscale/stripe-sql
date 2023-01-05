from sqlalchemy import Column, String


class Source_Transaction_Chf_Credit_Transfer_Data(Base):
    __tablename__ = "source_transaction_chf_credit_transfer_data"
    reference = Column(
        String, comment="Reference associated with the transfer", nullable=True
    )
    sender_address_country = Column(
        String, comment="Sender's country address", nullable=True
    )
    sender_address_line1 = Column(
        String, comment="Sender's line 1 address", nullable=True
    )
    sender_iban = Column(String, comment="Sender's bank account IBAN", nullable=True)
    sender_name = Column(
        String, comment="Sender's name", nullable=True, primary_key=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Transaction_Chf_Credit_Transfer_Data(reference={reference!r}, sender_address_country={sender_address_country!r}, sender_address_line1={sender_address_line1!r}, sender_iban={sender_iban!r}, sender_name={sender_name!r})".format(
            reference=self.reference,
            sender_address_country=self.sender_address_country,
            sender_address_line1=self.sender_address_line1,
            sender_iban=self.sender_iban,
            sender_name=self.sender_name,
        )


__all__ = ["source_transaction_chf_credit_transfer_data"]
