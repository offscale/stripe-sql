from sqlalchemy import Column, String

from . import Base


class OutboundPaymentsPaymentMethodDetailsFinancialAccount(Base):
    __tablename__ = "outbound_payments_payment_method_details_financial_account"
    id = Column(String, comment="Token of the FinancialAccount", primary_key=True)
    network = Column(String, comment="The rails used to send funds")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "OutboundPaymentsPaymentMethodDetailsFinancialAccount(id={id!r}, network={network!r})".format(
            id=self.id, network=self.network
        )


__all__ = ["outbound_payments_payment_method_details_financial_account"]
