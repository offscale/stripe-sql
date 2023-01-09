from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions(Base):
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
        return "InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions(permissions={permissions!r}, id={id!r})".format(
            permissions=self.permissions, id=self.id
        )


__all__ = ["invoice_payment_method_options_us_bank_account_linked_account_options"]
