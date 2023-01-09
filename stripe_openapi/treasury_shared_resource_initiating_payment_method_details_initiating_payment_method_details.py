from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails(
    Base
):
    __tablename__ = "treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details"
    balance = Column(String, comment="Set when `type` is `balance`", nullable=True)
    billing_details = Column(
        Integer, ForeignKey("treasury_shared_resource_billing_details.id")
    )
    financial_account = Column(
        String,
        ForeignKey("received_payment_method_details_financial_account.id"),
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
        String,
        ForeignKey(
            "treasury_shared_resource_initiating_payment_method_details_us_bank_account.bank_name"
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
        return "TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails(balance={balance!r}, billing_details={billing_details!r}, financial_account={financial_account!r}, issuing_card={issuing_card!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
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
