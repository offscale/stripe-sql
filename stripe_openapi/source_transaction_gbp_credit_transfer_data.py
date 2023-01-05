from sqlalchemy import Column, String


class Source_Transaction_Gbp_Credit_Transfer_Data(Base):
    __tablename__ = "source_transaction_gbp_credit_transfer_data"
    fingerprint = Column(
        String,
        comment="Bank account fingerprint associated with the Stripe owned bank account receiving the transfer",
        nullable=True,
    )
    funding_method = Column(
        String,
        comment="The credit transfer rails the sender used to push this transfer. The possible rails are: Faster Payments, BACS, CHAPS, and wire transfers. Currently only Faster Payments is supported",
        nullable=True,
    )
    last4 = Column(
        String,
        comment="Last 4 digits of sender account number associated with the transfer",
        nullable=True,
    )
    reference = Column(
        String,
        comment="Sender entered arbitrary information about the transfer",
        nullable=True,
    )
    sender_account_number = Column(
        String,
        comment="Sender account number associated with the transfer",
        nullable=True,
    )
    sender_name = Column(
        String,
        comment="Sender name associated with the transfer",
        nullable=True,
        primary_key=True,
    )
    sender_sort_code = Column(
        String, comment="Sender sort code associated with the transfer", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Transaction_Gbp_Credit_Transfer_Data(fingerprint={fingerprint!r}, funding_method={funding_method!r}, last4={last4!r}, reference={reference!r}, sender_account_number={sender_account_number!r}, sender_name={sender_name!r}, sender_sort_code={sender_sort_code!r})".format(
            fingerprint=self.fingerprint,
            funding_method=self.funding_method,
            last4=self.last4,
            reference=self.reference,
            sender_account_number=self.sender_account_number,
            sender_name=self.sender_name,
            sender_sort_code=self.sender_sort_code,
        )


__all__ = ["source_transaction_gbp_credit_transfer_data"]
