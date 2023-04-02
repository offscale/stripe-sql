from sqlalchemy import Column, String, Table

from . import metadata

IssuingAuthorizationNetworkDataJson = Table(
    "issuing_authorization_network_datajson",
    metadata,
    Column(
        "acquiring_institution_id",
        String,
        comment="Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["issuing_authorization_network_data.json"]
