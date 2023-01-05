from sqlalchemy import Boolean, Column, Integer, String


class Legal_Entity_Company(Base):
    __tablename__ = "legal_entity_company"
    address = Column(Address, nullable=True)
    address_kana = Column(
        LegalEntityJapanAddress,
        comment="The Kana variation of the company's primary address (Japan only)",
        nullable=True,
    )
    address_kanji = Column(
        LegalEntityJapanAddress,
        comment="The Kanji variation of the company's primary address (Japan only)",
        nullable=True,
    )
    directors_provided = Column(
        Boolean,
        comment="Whether the company's directors have been provided. This Boolean will be `true` if you've manually indicated that all directors are provided via [the `directors_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-directors_provided)",
        nullable=True,
    )
    executives_provided = Column(
        Boolean,
        comment="Whether the company's executives have been provided. This Boolean will be `true` if you've manually indicated that all executives are provided via [the `executives_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided",
        nullable=True,
    )
    name = Column(String, comment="The company's legal name", nullable=True)
    name_kana = Column(
        String,
        comment="The Kana variation of the company's legal name (Japan only)",
        nullable=True,
    )
    name_kanji = Column(
        String,
        comment="The Kanji variation of the company's legal name (Japan only)",
        nullable=True,
    )
    owners_provided = Column(
        Boolean,
        comment="Whether the company's owners have been provided. This Boolean will be `true` if you've manually indicated that all owners are provided via [the `owners_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together)",
        nullable=True,
    )
    ownership_declaration = Column(
        LegalEntityUboDeclaration,
        comment="This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct",
        nullable=True,
    )
    phone = Column(
        String,
        comment="The company's phone number (used for verification)",
        nullable=True,
    )
    structure = Column(
        String,
        comment="The category identifying the legal structure of the company or legal entity. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details",
        nullable=True,
    )
    tax_id_provided = Column(
        Boolean,
        comment="Whether the company's business ID number was provided",
        nullable=True,
    )
    tax_id_registrar = Column(
        String,
        comment="The jurisdiction in which the `tax_id` is registered (Germany-based companies only)",
        nullable=True,
    )
    vat_id_provided = Column(
        Boolean,
        comment="Whether the company's business VAT number was provided",
        nullable=True,
    )
    verification = Column(
        LegalEntityCompanyVerification,
        comment="Information on the verification state of the company",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Legal_Entity_Company(address={address!r}, address_kana={address_kana!r}, address_kanji={address_kanji!r}, directors_provided={directors_provided!r}, executives_provided={executives_provided!r}, name={name!r}, name_kana={name_kana!r}, name_kanji={name_kanji!r}, owners_provided={owners_provided!r}, ownership_declaration={ownership_declaration!r}, phone={phone!r}, structure={structure!r}, tax_id_provided={tax_id_provided!r}, tax_id_registrar={tax_id_registrar!r}, vat_id_provided={vat_id_provided!r}, verification={verification!r}, id={id!r})".format(
            address=self.address,
            address_kana=self.address_kana,
            address_kanji=self.address_kanji,
            directors_provided=self.directors_provided,
            executives_provided=self.executives_provided,
            name=self.name,
            name_kana=self.name_kana,
            name_kanji=self.name_kanji,
            owners_provided=self.owners_provided,
            ownership_declaration=self.ownership_declaration,
            phone=self.phone,
            structure=self.structure,
            tax_id_provided=self.tax_id_provided,
            tax_id_registrar=self.tax_id_registrar,
            vat_id_provided=self.vat_id_provided,
            verification=self.verification,
            id=self.id,
        )


__all__ = ["legal_entity_company"]
