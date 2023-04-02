from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.person import Person

from . import metadata

AccountJson = Table(
    "accountjson",
    metadata,
    Column(
        "business_profile",
        AccountBusinessProfile,
        ForeignKey("AccountBusinessProfile"),
        comment="Business information about the account",
        nullable=True,
    ),
    Column("business_type", String, comment="The business type", nullable=True),
    Column(
        "capabilities",
        AccountCapabilities,
        ForeignKey("AccountCapabilities"),
        nullable=True,
    ),
    Column(
        "charges_enabled",
        Boolean,
        comment="Whether the account can create live charges",
        nullable=True,
    ),
    Column(
        "company", LegalEntityCompany, ForeignKey("LegalEntityCompany"), nullable=True
    ),
    Column(
        "controller",
        AccountUnificationAccountController,
        ForeignKey("AccountUnificationAccountController"),
        nullable=True,
    ),
    Column("country", String, comment="The account's country", nullable=True),
    Column(
        "created",
        Integer,
        comment="Time at which the account was connected. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "default_currency",
        String,
        comment="Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts)",
        nullable=True,
    ),
    Column(
        "details_submitted",
        Boolean,
        comment="Whether account details have been submitted. Standard accounts cannot receive payouts before this is true",
        nullable=True,
    ),
    Column(
        "email",
        String,
        comment="An email address associated with the account. You can treat this as metadata: it is not used for authentication or messaging account holders",
        nullable=True,
    ),
    Column(
        "external_accounts",
        JSON,
        comment="External accounts (bank accounts and debit cards) currently attached to this account",
        nullable=True,
    ),
    Column(
        "future_requirements",
        AccountFutureRequirements,
        ForeignKey("AccountFutureRequirements"),
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("individual", Person, ForeignKey("Person"), nullable=True),
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
        "payouts_enabled",
        Boolean,
        comment="Whether Stripe can send payouts to this account",
        nullable=True,
    ),
    Column(
        "requirements",
        AccountRequirements,
        ForeignKey("AccountRequirements"),
        nullable=True,
    ),
    Column(
        "settings",
        AccountSettings,
        ForeignKey("AccountSettings"),
        comment="Options for customizing how the account functions within Stripe",
        nullable=True,
    ),
    Column(
        "tos_acceptance",
        AccountTosAcceptance,
        ForeignKey("AccountTosAcceptance"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The Stripe account type. Can be `standard`, `express`, or `custom`",
        nullable=True,
    ),
)
__all__ = ["account.json"]
