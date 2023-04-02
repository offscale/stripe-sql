from sqlalchemy import Boolean, Column, Table

from . import metadata

IssuingCardholderCompanyJson = Table(
    "issuing_cardholder_companyjson",
    metadata,
    Column(
        "tax_id_provided",
        Boolean,
        comment="Whether the company's business ID number was provided",
        primary_key=True,
    ),
)
__all__ = ["issuing_cardholder_company.json"]
