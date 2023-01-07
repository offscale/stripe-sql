from sqlalchemy import Column, Integer, String


class Outbound_Payments_Payment_Method_Details(Base):
    __tablename__ = "outbound_payments_payment_method_details"
    billing_details = Column(
        treasury_shared_resource_billing_details,
        ForeignKey("treasury_shared_resource_billing_details"),
    )
    financial_account = Column(
        outbound_payments_payment_method_details_financial_account,
        ForeignKey("outbound_payments_payment_method_details_financial_account"),
        nullable=True,
    )
    type = Column(
        String, comment="The type of the payment method used in the OutboundPayment"
    )
    us_bank_account = Column(
        outbound_payments_payment_method_details_us_bank_account,
        ForeignKey("outbound_payments_payment_method_details_us_bank_account"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Outbound_Payments_Payment_Method_Details(billing_details={billing_details!r}, financial_account={financial_account!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            billing_details=self.billing_details,
            financial_account=self.financial_account,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["outbound_payments_payment_method_details"]
