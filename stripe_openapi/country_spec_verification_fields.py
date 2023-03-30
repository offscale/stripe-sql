from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

CountrySpecVerificationFields.Json = Table(
    "country_spec_verification_fields.json",
    metadata,
    Column(
        "company",
        CountrySpecVerificationFieldDetails,
        ForeignKey("CountrySpecVerificationFieldDetails"),
    ),
    Column(
        "individual",
        CountrySpecVerificationFieldDetails,
        ForeignKey("CountrySpecVerificationFieldDetails"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["country_spec_verification_fields.json"]
