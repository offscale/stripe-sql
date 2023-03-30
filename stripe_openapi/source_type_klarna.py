from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeKlarna.Json = Table(
    "source_type_klarna.json",
    metadata,
    Column("background_image_url", String, nullable=True),
    Column("client_token", String, nullable=True),
    Column("first_name", String, nullable=True),
    Column("last_name", String, nullable=True),
    Column("locale", String, nullable=True),
    Column("logo_url", String, nullable=True),
    Column("page_title", String, nullable=True),
    Column("pay_later_asset_urls_descriptive", String, nullable=True),
    Column("pay_later_asset_urls_standard", String, nullable=True),
    Column("pay_later_name", String, nullable=True),
    Column("pay_later_redirect_url", String, nullable=True),
    Column("pay_now_asset_urls_descriptive", String, nullable=True),
    Column("pay_now_asset_urls_standard", String, nullable=True),
    Column("pay_now_name", String, nullable=True),
    Column("pay_now_redirect_url", String, nullable=True),
    Column("pay_over_time_asset_urls_descriptive", String, nullable=True),
    Column("pay_over_time_asset_urls_standard", String, nullable=True),
    Column("pay_over_time_name", String, nullable=True),
    Column("pay_over_time_redirect_url", String, nullable=True),
    Column("payment_method_categories", String, nullable=True),
    Column("purchase_country", String, nullable=True),
    Column("purchase_type", String, nullable=True),
    Column("redirect_url", String, nullable=True),
    Column("shipping_delay", Integer, nullable=True),
    Column("shipping_first_name", String, nullable=True),
    Column("shipping_last_name", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_klarna.json"]
