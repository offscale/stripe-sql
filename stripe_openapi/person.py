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

from stripe_openapi.address import Address

from . import metadata

PersonJson = Table(
    "personjson",
    metadata,
    Column(
        "account",
        String,
        comment="The account the person is associated with",
        nullable=True,
    ),
    Column("address", Address, ForeignKey("Address"), nullable=True),
    Column(
        "address_kana",
        LegalEntityJapanAddress,
        ForeignKey("LegalEntityJapanAddress"),
        comment="The Kana variation of the person's address (Japan only)",
        nullable=True,
    ),
    Column(
        "address_kanji",
        LegalEntityJapanAddress,
        ForeignKey("LegalEntityJapanAddress"),
        comment="The Kanji variation of the person's address (Japan only)",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("dob", LegalEntityDob, ForeignKey("LegalEntityDob"), nullable=True),
    Column("email", String, comment="The person's email address", nullable=True),
    Column("first_name", String, comment="The person's first name", nullable=True),
    Column(
        "first_name_kana",
        String,
        comment="The Kana variation of the person's first name (Japan only)",
        nullable=True,
    ),
    Column(
        "first_name_kanji",
        String,
        comment="The Kanji variation of the person's first name (Japan only)",
        nullable=True,
    ),
    Column(
        "full_name_aliases",
        ARRAY(String),
        comment="A list of alternate names or aliases that the person is known by",
        nullable=True,
    ),
    Column(
        "future_requirements",
        PersonFutureRequirements,
        ForeignKey("PersonFutureRequirements"),
        comment="Information about the upcoming new requirements for this person, including what information needs to be collected, and by when",
        nullable=True,
    ),
    Column(
        "gender",
        String,
        comment='The person\'s gender (International regulations require either "male" or "female")',
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column(
        "id_number_provided",
        Boolean,
        comment="Whether the person's `id_number` was provided",
        nullable=True,
    ),
    Column(
        "id_number_secondary_provided",
        Boolean,
        comment="Whether the person's `id_number_secondary` was provided",
        nullable=True,
    ),
    Column("last_name", String, comment="The person's last name", nullable=True),
    Column(
        "last_name_kana",
        String,
        comment="The Kana variation of the person's last name (Japan only)",
        nullable=True,
    ),
    Column(
        "last_name_kanji",
        String,
        comment="The Kanji variation of the person's last name (Japan only)",
        nullable=True,
    ),
    Column("maiden_name", String, comment="The person's maiden name", nullable=True),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "nationality",
        String,
        comment="The country where the person is a national",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("phone", String, comment="The person's phone number", nullable=True),
    Column(
        "political_exposure",
        String,
        comment="Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction",
        nullable=True,
    ),
    Column("registered_address", Address, ForeignKey("Address"), nullable=True),
    Column(
        "relationship",
        PersonRelationship,
        ForeignKey("PersonRelationship"),
        nullable=True,
    ),
    Column(
        "requirements",
        PersonRequirements,
        ForeignKey("PersonRequirements"),
        comment="Information about the requirements for this person, including what information needs to be collected, and by when",
        nullable=True,
    ),
    Column(
        "ssn_last_4_provided",
        Boolean,
        comment="Whether the last four digits of the person's Social Security number have been provided (U.S. only)",
        nullable=True,
    ),
    Column(
        "verification",
        LegalEntityPersonVerification,
        ForeignKey("LegalEntityPersonVerification"),
        nullable=True,
    ),
)
__all__ = ["person.json"]
