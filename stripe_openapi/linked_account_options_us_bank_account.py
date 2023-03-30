from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

LinkedAccountOptionsUsBankAccount.Json = Table(
    "linked_account_options_us_bank_account.json",
    metadata,
    Column(
        "permissions",
        ARRAY(String),
        comment="The list of permissions to request. The `payment_method` permission must be included",
        nullable=True,
    ),
    Column(
        "return_url",
        String,
        comment="For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["linked_account_options_us_bank_account.json"]
