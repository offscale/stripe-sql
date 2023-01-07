from sqlalchemy import Column, Integer, String


class Treasury_Shared_Resource_Initiating_Payment_Method_Details_Initiating_Payment_Method_Details(
    Base
):
    __tablename__ = "treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details"
    balance = Column(String, comment="Set when `type` is `balance`", nullable=True)
    billing_details = Column(
        treasury_shared_resource_billing_details,
        ForeignKey("treasury_shared_resource_billing_details"),
    )
    financial_account = Column(
        received_payment_method_details_financial_account,
        ForeignKey("received_payment_method_details_financial_account"),
        nullable=True,
    )
    issuing_card = Column(
        String,
        comment="Set when `type` is `issuing_card`. This is an [Issuing Card](https://stripe.com/docs/api#issuing_cards) ID",
        nullable=True,
    )
    type = Column(
        String,
        comment="Polymorphic type matching the originating money movement's source. This can be an external account, a Stripe balance, or a FinancialAccount",
    )
    us_bank_account = Column(
        treasury_shared_resource_initiating_payment_method_details_us_bank_account,
        ForeignKey(
            "treasury_shared_resource_initiating_payment_method_details_us_bank_account"
        ),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Shared_Resource_Initiating_Payment_Method_Details_Initiating_Payment_Method_Details(balance={balance!r}, billing_details={billing_details!r}, financial_account={financial_account!r}, issuing_card={issuing_card!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            balance=self.balance,
            billing_details=self.billing_details,
            financial_account=self.financial_account,
            issuing_card=self.issuing_card,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = [
    "treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details"
]
