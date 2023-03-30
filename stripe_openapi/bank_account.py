from sqlalchemy import (
    ARRAY,
    JSON,
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
)

from stripe_openapi.account import Account
from stripe_openapi.customer import Customer

from . import metadata

BankAccount.Json = Table(
    "bank_account.json",
    metadata,
    Column(
        "account",
        Account,
        ForeignKey("Account"),
        comment="The ID of the account that the bank account is associated with",
        nullable=True,
    ),
    Column(
        "account_holder_name",
        String,
        comment="The name of the person or business that owns the bank account",
        nullable=True,
    ),
    Column(
        "account_holder_type",
        String,
        comment="The type of entity that holds the account. This can be either `individual` or `company`",
        nullable=True,
    ),
    Column(
        "account_type",
        String,
        comment="The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`",
        nullable=True,
    ),
    Column(
        "available_payout_methods",
        ARRAY(String),
        comment="A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout",
        nullable=True,
    ),
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the routing number (e.g., `WELLS FARGO`)",
        nullable=True,
    ),
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country the bank account is located in",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account",
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The ID of the customer that the bank account is associated with",
        nullable=True,
    ),
    Column(
        "default_for_currency",
        Boolean,
        comment="Whether this bank account is the default external account for its currency",
        nullable=True,
    ),
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    ),
    Column(
        "future_requirements",
        ExternalAccountRequirements,
        ForeignKey("ExternalAccountRequirements"),
        comment="Information about upcoming new requirements for the bank account, including what information needs to be collected",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column("last4", String, comment="The last four digits of the bank account number"),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "requirements",
        ExternalAccountRequirements,
        ForeignKey("ExternalAccountRequirements"),
        comment="Information about the requirements for the bank account, including what information needs to be collected",
        nullable=True,
    ),
    Column(
        "routing_number",
        String,
        comment="The routing transit number for the bank account",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a transfer sent to this bank account fails, we'll set the status to `errored` and will not continue to send transfers until the bank details are updated.\n\nFor external accounts, possible values are `new`, `errored` and `verification_failed`. If a transfer fails, the status is set to `errored` and transfers are stopped until account details are updated. In India, if we can't [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we'll set the status to `verification_failed`. Other validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply",
    ),
)
__all__ = ["bank_account.json"]
