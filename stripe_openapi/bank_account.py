from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, String

from . import Base


class BankAccount(Base):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
    destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank Debits and Transfers](https://stripe.com/docs/payments/bank-debits-transfers).

    """

    __tablename__ = "bank_account"
    account = Column(
        Account,
        ForeignKey("Account"),
        comment="The ID of the account that the bank account is associated with",
        nullable=True,
    )
    account_holder_name = Column(
        String,
        comment="The name of the person or business that owns the bank account",
        nullable=True,
    )
    account_holder_type = Column(
        String,
        comment="The type of entity that holds the account. This can be either `individual` or `company`",
        nullable=True,
    )
    account_type = Column(
        String,
        comment="The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`",
        nullable=True,
    )
    available_payout_methods = Column(
        ARRAY(String),
        comment="A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout",
        nullable=True,
    )
    bank_name = Column(
        String,
        comment="Name of the bank associated with the routing number (e.g., `WELLS FARGO`)",
        nullable=True,
    )
    country = Column(
        String,
        comment="Two-letter ISO code representing the country the bank account is located in",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account",
    )
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The ID of the customer that the bank account is associated with",
        nullable=True,
    )
    default_for_currency = Column(
        Boolean,
        comment="Whether this bank account is the default external account for its currency",
        nullable=True,
    )
    fingerprint = Column(
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    last4 = Column(String, comment="The last four digits of the bank account number")
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    routing_number = Column(
        String, comment="The routing transit number for the bank account", nullable=True
    )
    status = Column(
        String,
        comment="For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a transfer sent to this bank account fails, we'll set the status to `errored` and will not continue to send transfers until the bank details are updated.\n\nFor external accounts, possible values are `new` and `errored`. Validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply. If a transfer fails, the status is set to `errored` and transfers are stopped until account details are updated",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "BankAccount(account={account!r}, account_holder_name={account_holder_name!r}, account_holder_type={account_holder_type!r}, account_type={account_type!r}, available_payout_methods={available_payout_methods!r}, bank_name={bank_name!r}, country={country!r}, currency={currency!r}, customer={customer!r}, default_for_currency={default_for_currency!r}, fingerprint={fingerprint!r}, id={id!r}, last4={last4!r}, metadata={metadata!r}, object={object!r}, routing_number={routing_number!r}, status={status!r})".format(
            account=self.account,
            account_holder_name=self.account_holder_name,
            account_holder_type=self.account_holder_type,
            account_type=self.account_type,
            available_payout_methods=self.available_payout_methods,
            bank_name=self.bank_name,
            country=self.country,
            currency=self.currency,
            customer=self.customer,
            default_for_currency=self.default_for_currency,
            fingerprint=self.fingerprint,
            id=self.id,
            last4=self.last4,
            metadata=self.metadata,
            object=self.object,
            routing_number=self.routing_number,
            status=self.status,
        )


__all__ = ["bank_account"]
