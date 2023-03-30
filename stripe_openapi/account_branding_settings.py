from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

AccountBrandingSettings.Json = Table(
    "account_branding_settings.json",
    metadata,
    Column(
        "icon",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px",
        nullable=True,
    ),
    Column(
        "logo",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px",
        nullable=True,
    ),
    Column(
        "primary_color",
        String,
        comment="A CSS hex color value representing the primary branding color for this account",
        nullable=True,
    ),
    Column(
        "secondary_color",
        String,
        comment="A CSS hex color value representing the secondary branding color for this account",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_branding_settings.json"]
