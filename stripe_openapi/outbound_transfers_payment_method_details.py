from sqlalchemy import Column, Integer, String


class Outbound_Transfers_Payment_Method_Details(Base):
    __tablename__ = "outbound_transfers_payment_method_details"
    billing_details = Column(TreasurySharedResourceBillingDetails)
    type = Column(
        String, comment="The type of the payment method used in the OutboundTransfer"
    )
    us_bank_account = Column(
        OutboundTransfersPaymentMethodDetailsUsBankAccount, nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Outbound_Transfers_Payment_Method_Details(billing_details={billing_details!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            billing_details=self.billing_details,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["outbound_transfers_payment_method_details"]
