from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingCardShippingCustomsJson = Table(
    "issuing_card_shipping_customsjson",
    metadata,
    Column(
        "eori_number",
        String,
        comment="A registration number used for customs in Europe. See https://www.gov.uk/eori and https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_card_shipping_customs.json"]
