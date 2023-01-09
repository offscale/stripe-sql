from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String

from stripe_openapi.legal_entity_japan_address import LegalEntityJapanAddress
from stripe_openapi.person_future_requirements import PersonFutureRequirements
from stripe_openapi.person_requirements import PersonRequirements

from . import Base


class Person(Base):
    """
    This is an object representing a person associated with a Stripe account.

    A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
    See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform pre-filling and account onboarding steps.

    Related guide: [Handling Identity Verification with the API](https://stripe.com/docs/connect/identity-verification-api#person-information).

    """

    __tablename__ = "person"
    account = Column(
        String, comment="The account the person is associated with", nullable=True
    )
    address = Column(Address, ForeignKey("Address"), nullable=True)
    address_kana = Column(
        LegalEntityJapanAddress,
        comment="[[FK(LegalEntityJapanAddress)]] The Kana variation of the person's address (Japan only)",
        nullable=True,
    )
    address_kanji = Column(
        LegalEntityJapanAddress,
        comment="[[FK(LegalEntityJapanAddress)]] The Kanji variation of the person's address (Japan only)",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    dob = Column(Integer, ForeignKey("legal_entity_dob.id"), nullable=True)
    email = Column(String, comment="The person's email address", nullable=True)
    first_name = Column(String, comment="The person's first name", nullable=True)
    first_name_kana = Column(
        String,
        comment="The Kana variation of the person's first name (Japan only)",
        nullable=True,
    )
    first_name_kanji = Column(
        String,
        comment="The Kanji variation of the person's first name (Japan only)",
        nullable=True,
    )
    full_name_aliases = Column(
        ARRAY(String),
        comment="A list of alternate names or aliases that the person is known by",
        nullable=True,
    )
    future_requirements = Column(
        PersonFutureRequirements,
        comment="[[FK(PersonFutureRequirements)]] Information about the upcoming new requirements for this person, including what information needs to be collected, and by when",
        nullable=True,
    )
    gender = Column(
        String,
        comment='The person\'s gender (International regulations require either "male" or "female")',
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    id_number_provided = Column(
        Boolean, comment="Whether the person's `id_number` was provided", nullable=True
    )
    id_number_secondary_provided = Column(
        Boolean,
        comment="Whether the person's `id_number_secondary` was provided",
        nullable=True,
    )
    last_name = Column(String, comment="The person's last name", nullable=True)
    last_name_kana = Column(
        String,
        comment="The Kana variation of the person's last name (Japan only)",
        nullable=True,
    )
    last_name_kanji = Column(
        String,
        comment="The Kanji variation of the person's last name (Japan only)",
        nullable=True,
    )
    maiden_name = Column(String, comment="The person's maiden name", nullable=True)
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    nationality = Column(
        String, comment="The country where the person is a national", nullable=True
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    phone = Column(String, comment="The person's phone number", nullable=True)
    political_exposure = Column(
        String,
        comment="Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction",
        nullable=True,
    )
    registered_address = Column(Address, ForeignKey("Address"), nullable=True)
    relationship = Column(Integer, ForeignKey("person_relationship.id"), nullable=True)
    requirements = Column(
        PersonRequirements,
        comment="[[FK(PersonRequirements)]] Information about the requirements for this person, including what information needs to be collected, and by when",
        nullable=True,
    )
    ssn_last_4_provided = Column(
        Boolean,
        comment="Whether the last four digits of the person's Social Security number have been provided (U.S. only)",
        nullable=True,
    )
    verification = Column(
        Integer, ForeignKey("legal_entity_person_verification.id"), nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Person(account={account!r}, address={address!r}, address_kana={address_kana!r}, address_kanji={address_kanji!r}, created={created!r}, dob={dob!r}, email={email!r}, first_name={first_name!r}, first_name_kana={first_name_kana!r}, first_name_kanji={first_name_kanji!r}, full_name_aliases={full_name_aliases!r}, future_requirements={future_requirements!r}, gender={gender!r}, id={id!r}, id_number_provided={id_number_provided!r}, id_number_secondary_provided={id_number_secondary_provided!r}, last_name={last_name!r}, last_name_kana={last_name_kana!r}, last_name_kanji={last_name_kanji!r}, maiden_name={maiden_name!r}, metadata={metadata!r}, nationality={nationality!r}, object={object!r}, phone={phone!r}, political_exposure={political_exposure!r}, registered_address={registered_address!r}, relationship={relationship!r}, requirements={requirements!r}, ssn_last_4_provided={ssn_last_4_provided!r}, verification={verification!r})".format(
            account=self.account,
            address=self.address,
            address_kana=self.address_kana,
            address_kanji=self.address_kanji,
            created=self.created,
            dob=self.dob,
            email=self.email,
            first_name=self.first_name,
            first_name_kana=self.first_name_kana,
            first_name_kanji=self.first_name_kanji,
            full_name_aliases=self.full_name_aliases,
            future_requirements=self.future_requirements,
            gender=self.gender,
            id=self.id,
            id_number_provided=self.id_number_provided,
            id_number_secondary_provided=self.id_number_secondary_provided,
            last_name=self.last_name,
            last_name_kana=self.last_name_kana,
            last_name_kanji=self.last_name_kanji,
            maiden_name=self.maiden_name,
            metadata=self.metadata,
            nationality=self.nationality,
            object=self.object,
            phone=self.phone,
            political_exposure=self.political_exposure,
            registered_address=self.registered_address,
            relationship=self.relationship,
            requirements=self.requirements,
            ssn_last_4_provided=self.ssn_last_4_provided,
            verification=self.verification,
        )


__all__ = ["person"]
