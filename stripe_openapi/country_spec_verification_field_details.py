from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

CountrySpecVerificationFieldDetailsJson = Table(
    "country_spec_verification_field_detailsjson",
    metadata,
    Column(
        "additional",
        ARRAY(String),
        comment="Additional fields which are only required for some users",
    ),
    Column(
        "minimum",
        ARRAY(String),
        comment="Fields which every account must eventually provide",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["country_spec_verification_field_details.json"]
