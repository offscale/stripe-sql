from sqlalchemy import Column, Integer, String


class Payment_Method_Options_Customer_Balance_Bank_Transfer(Base):
    __tablename__ = "payment_method_options_customer_balance_bank_transfer"
    eu_bank_transfer = Column(
        PaymentMethodOptionsCustomerBalanceEuBankAccount, nullable=True
    )
    requested_address_types = Column(
        ARRAY(String),
        comment="List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.\n\nPermitted values include: `sort_code`, `zengin`, `iban`, or `spei`",
        nullable=True,
    )
    type = Column(
        String,
        comment="The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, or `mx_bank_transfer`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Method_Options_Customer_Balance_Bank_Transfer(eu_bank_transfer={eu_bank_transfer!r}, requested_address_types={requested_address_types!r}, type={type!r}, id={id!r})".format(
            eu_bank_transfer=self.eu_bank_transfer,
            requested_address_types=self.requested_address_types,
            type=self.type,
            id=self.id,
        )


__all__ = ["payment_method_options_customer_balance_bank_transfer"]
