from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

ThreeDSecureDetails.Json = Table(
    "three_d_secure_details.json",
    metadata,
    Column(
        "authentication_flow",
        String,
        comment="For authenticated transactions: how the customer was authenticated by\nthe issuing bank",
        nullable=True,
    ),
    Column(
        "result",
        String,
        comment="Indicates the outcome of 3D Secure authentication",
        nullable=True,
    ),
    Column(
        "result_reason",
        String,
        comment="Additional information about why 3D Secure succeeded or failed based\non the `result`",
        nullable=True,
    ),
    Column(
        "version",
        String,
        comment="The version of 3D Secure that was used",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["three_d_secure_details.json"]
