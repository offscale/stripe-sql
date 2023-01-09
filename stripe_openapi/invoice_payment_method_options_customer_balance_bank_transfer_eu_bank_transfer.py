from sqlalchemy import Column, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(Base):
    __tablename__ = (
        "invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer"
    )
    country = Column(
        String,
        comment="The desired country code of the bank account information. Permitted values include: `DE`, `ES`, `FR`, `IE`, or `NL`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(country={country!r}, id={id!r})".format(
            country=self.country, id=self.id
        )


__all__ = [
    "invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer"
]
