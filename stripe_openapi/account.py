from sqlalchemy import Boolean, Column, Integer, String


class Account(Base):
    """
    This is an object representing a Stripe account. You can retrieve it to see

    properties on the account like its current e-mail address or if the account is
    enabled yet to make live charges.

    Some properties, marked below, are available only to platforms that want to
    [create and manage Express or Custom accounts](https://stripe.com/docs/connect/accounts).

    """

    __tablename__ = "account"
    business_profile = Column(
        account_business_profile,
        comment="[[FK(account_business_profile)]] Business information about the account",
        nullable=True,
    )
    business_type = Column(String, comment="The business type", nullable=True)
    capabilities = Column(
        account_capabilities, ForeignKey("account_capabilities"), nullable=True
    )
    charges_enabled = Column(
        Boolean, comment="Whether the account can create live charges", nullable=True
    )
    company = Column(
        legal_entity_company, ForeignKey("legal_entity_company"), nullable=True
    )
    controller = Column(
        account_unification_account_controller,
        ForeignKey("account_unification_account_controller"),
        nullable=True,
    )
    country = Column(String, comment="The account's country", nullable=True)
    created = Column(
        Integer,
        comment="Time at which the account was connected. Measured in seconds since the Unix epoch",
        nullable=True,
    )
    default_currency = Column(
        String,
        comment="Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts)",
        nullable=True,
    )
    details_submitted = Column(
        Boolean,
        comment="Whether account details have been submitted. Standard accounts cannot receive payouts before this is true",
        nullable=True,
    )
    email = Column(
        String,
        comment="An email address associated with the account. You can treat this as metadata: it is not used for authentication or messaging account holders",
        nullable=True,
    )
    external_accounts = Column(
        JSON,
        comment="External accounts (bank accounts and debit cards) currently attached to this account",
        nullable=True,
    )
    future_requirements = Column(
        account_future_requirements,
        ForeignKey("account_future_requirements"),
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    individual = Column(person, ForeignKey("person"), nullable=True)
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    payouts_enabled = Column(
        Boolean,
        comment="Whether Stripe can send payouts to this account",
        nullable=True,
    )
    requirements = Column(
        account_requirements, ForeignKey("account_requirements"), nullable=True
    )
    settings = Column(
        account_settings,
        comment="[[FK(account_settings)]] Options for customizing how the account functions within Stripe",
        nullable=True,
    )
    tos_acceptance = Column(
        account_tos_acceptance, ForeignKey("account_tos_acceptance"), nullable=True
    )
    type = Column(
        String,
        comment="The Stripe account type. Can be `standard`, `express`, or `custom`",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account(business_profile={business_profile!r}, business_type={business_type!r}, capabilities={capabilities!r}, charges_enabled={charges_enabled!r}, company={company!r}, controller={controller!r}, country={country!r}, created={created!r}, default_currency={default_currency!r}, details_submitted={details_submitted!r}, email={email!r}, external_accounts={external_accounts!r}, future_requirements={future_requirements!r}, id={id!r}, individual={individual!r}, metadata={metadata!r}, object={object!r}, payouts_enabled={payouts_enabled!r}, requirements={requirements!r}, settings={settings!r}, tos_acceptance={tos_acceptance!r}, type={type!r})".format(
            business_profile=self.business_profile,
            business_type=self.business_type,
            capabilities=self.capabilities,
            charges_enabled=self.charges_enabled,
            company=self.company,
            controller=self.controller,
            country=self.country,
            created=self.created,
            default_currency=self.default_currency,
            details_submitted=self.details_submitted,
            email=self.email,
            external_accounts=self.external_accounts,
            future_requirements=self.future_requirements,
            id=self.id,
            individual=self.individual,
            metadata=self.metadata,
            object=self.object,
            payouts_enabled=self.payouts_enabled,
            requirements=self.requirements,
            settings=self.settings,
            tos_acceptance=self.tos_acceptance,
            type=self.type,
        )


__all__ = ["account"]
