from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AccountPaymentsSettingsJson = Table(
    "account_payments_settingsjson",
    metadata,
    Column(
        "statement_descriptor",
        String,
        comment="The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge",
        nullable=True,
    ),
    Column(
        "statement_descriptor_kana",
        String,
        comment="The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only)",
        nullable=True,
    ),
    Column(
        "statement_descriptor_kanji",
        String,
        comment="The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only)",
        nullable=True,
    ),
    Column(
        "statement_descriptor_prefix_kana",
        String,
        comment="The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion",
        nullable=True,
    ),
    Column(
        "statement_descriptor_prefix_kanji",
        String,
        comment="The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_payments_settings.json"]
