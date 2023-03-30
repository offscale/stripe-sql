from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

IssuingCardholderIndividual.Json = Table(
    "issuing_cardholder_individual.json",
    metadata,
    Column(
        "card_issuing",
        IssuingCardholderCardIssuing,
        ForeignKey("IssuingCardholderCardIssuing"),
        comment="Information related to the card_issuing program for this cardholder",
        nullable=True,
    ),
    Column(
        "dob",
        IssuingCardholderIndividualDob,
        ForeignKey("IssuingCardholderIndividualDob"),
        comment="The date of birth of this cardholder",
        nullable=True,
    ),
    Column(
        "first_name",
        String,
        comment="The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters",
        nullable=True,
    ),
    Column(
        "last_name",
        String,
        comment="The last name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters",
        nullable=True,
    ),
    Column(
        "verification",
        IssuingCardholderVerification,
        ForeignKey("IssuingCardholderVerification"),
        comment="Government-issued ID document for this cardholder",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_individual.json"]
