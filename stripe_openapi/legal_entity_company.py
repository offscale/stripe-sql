from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

LegalEntityCompany.Json = Table(
    "legal_entity_company.json",
    metadata,
    Column("address", Address, ForeignKey("Address"), nullable=True),
    Column(
        "address_kana",
        LegalEntityJapanAddress,
        ForeignKey("LegalEntityJapanAddress"),
        comment="The Kana variation of the company's primary address (Japan only)",
        nullable=True,
    ),
    Column(
        "address_kanji",
        LegalEntityJapanAddress,
        ForeignKey("LegalEntityJapanAddress"),
        comment="The Kanji variation of the company's primary address (Japan only)",
        nullable=True,
    ),
    Column(
        "directors_provided",
        Boolean,
        comment="Whether the company's directors have been provided. This Boolean will be `true` if you've manually indicated that all directors are provided via [the `directors_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-directors_provided)",
        nullable=True,
    ),
    Column(
        "executives_provided",
        Boolean,
        comment="Whether the company's executives have been provided. This Boolean will be `true` if you've manually indicated that all executives are provided via [the `executives_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided",
        nullable=True,
    ),
    Column(
        "export_license_id",
        String,
        comment="The export license ID number of the company, also referred as Import Export Code (India only)",
        nullable=True,
    ),
    Column(
        "export_purpose_code",
        String,
        comment="The purpose code to use for export transactions (India only)",
        nullable=True,
    ),
    Column("name", String, comment="The company's legal name", nullable=True),
    Column(
        "name_kana",
        String,
        comment="The Kana variation of the company's legal name (Japan only)",
        nullable=True,
    ),
    Column(
        "name_kanji",
        String,
        comment="The Kanji variation of the company's legal name (Japan only)",
        nullable=True,
    ),
    Column(
        "owners_provided",
        Boolean,
        comment="Whether the company's owners have been provided. This Boolean will be `true` if you've manually indicated that all owners are provided via [the `owners_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together)",
        nullable=True,
    ),
    Column(
        "ownership_declaration",
        LegalEntityUboDeclaration,
        ForeignKey("LegalEntityUboDeclaration"),
        comment="This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct",
        nullable=True,
    ),
    Column(
        "phone",
        String,
        comment="The company's phone number (used for verification)",
        nullable=True,
    ),
    Column(
        "structure",
        String,
        comment="The category identifying the legal structure of the company or legal entity. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details",
        nullable=True,
    ),
    Column(
        "tax_id_provided",
        Boolean,
        comment="Whether the company's business ID number was provided",
        nullable=True,
    ),
    Column(
        "tax_id_registrar",
        String,
        comment="The jurisdiction in which the `tax_id` is registered (Germany-based companies only)",
        nullable=True,
    ),
    Column(
        "vat_id_provided",
        Boolean,
        comment="Whether the company's business VAT number was provided",
        nullable=True,
    ),
    Column(
        "verification",
        LegalEntityCompanyVerification,
        ForeignKey("LegalEntityCompanyVerification"),
        comment="Information on the verification state of the company",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_company.json"]
