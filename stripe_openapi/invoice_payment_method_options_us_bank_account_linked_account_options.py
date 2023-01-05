from sqlalchemy import Column, Integer


class Invoice_Payment_Method_Options_Us_Bank_Account_Linked_Account_Options(Base):
    __tablename__ = (
        "invoice_payment_method_options_us_bank_account_linked_account_options"
    )
    permissions = Column(
        ARRAY(String),
        comment="The list of permissions to request. The `payment_method` permission must be included",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Payment_Method_Options_Us_Bank_Account_Linked_Account_Options(permissions={permissions!r}, id={id!r})".format(
            permissions=self.permissions, id=self.id
        )


__all__ = ["invoice_payment_method_options_us_bank_account_linked_account_options"]
