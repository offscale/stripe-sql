from sqlalchemy import Column, String

from . import Base


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer(
    Base
):
    __tablename__ = "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer"
    bic = Column(
        String,
        comment="The BIC of the bank of the sender of the funding",
        nullable=True,
    )
    iban_last4 = Column(
        String,
        comment="The last 4 digits of the IBAN of the sender of the funding",
        nullable=True,
    )
    sender_name = Column(
        String,
        comment="The full name of the sender, as supplied by the sending bank",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer(bic={bic!r}, iban_last4={iban_last4!r}, sender_name={sender_name!r})".format(
            bic=self.bic, iban_last4=self.iban_last4, sender_name=self.sender_name
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer"
]
