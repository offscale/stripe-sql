from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsCustomerBalanceBankTransfer(Base):
    __tablename__ = "invoice_payment_method_options_customer_balance_bank_transfer"
    eu_bank_transfer = Column(
        Integer,
        ForeignKey(
            "invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer.id"
        ),
        nullable=True,
    )
    type = Column(
        String,
        comment="The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsCustomerBalanceBankTransfer(eu_bank_transfer={eu_bank_transfer!r}, type={type!r}, id={id!r})".format(
            eu_bank_transfer=self.eu_bank_transfer, type=self.type, id=self.id
        )


__all__ = ["invoice_payment_method_options_customer_balance_bank_transfer"]
