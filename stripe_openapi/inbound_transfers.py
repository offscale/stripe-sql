from sqlalchemy import Column, Integer, String


class Inbound_Transfers(Base):
    __tablename__ = "inbound_transfers"
    billing_details = Column(
        treasury_shared_resource_billing_details,
        ForeignKey("treasury_shared_resource_billing_details"),
    )
    type = Column(
        String, comment="The type of the payment method used in the InboundTransfer"
    )
    us_bank_account = Column(
        inbound_transfers_payment_method_details_us_bank_account,
        ForeignKey("inbound_transfers_payment_method_details_us_bank_account"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Inbound_Transfers(billing_details={billing_details!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            billing_details=self.billing_details,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["inbound_transfers"]
