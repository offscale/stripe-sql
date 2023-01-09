from sqlalchemy import Boolean, Column, Identity, Integer, String

from . import Base


class CustomerBalanceCustomerBalanceSettings(Base):
    __tablename__ = "customer_balance_customer_balance_settings"
    reconciliation_mode = Column(
        String,
        comment="The configuration for how funds that land in the customer cash balance are reconciled",
    )
    using_merchant_default = Column(
        Boolean,
        comment="A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerBalanceCustomerBalanceSettings(reconciliation_mode={reconciliation_mode!r}, using_merchant_default={using_merchant_default!r}, id={id!r})".format(
            reconciliation_mode=self.reconciliation_mode,
            using_merchant_default=self.using_merchant_default,
            id=self.id,
        )


__all__ = ["customer_balance_customer_balance_settings"]
