from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

AccountCardPaymentsSettingsJson = Table(
    "account_card_payments_settingsjson",
    metadata,
    Column(
        "decline_on",
        AccountDeclineChargeOn,
        ForeignKey("AccountDeclineChargeOn"),
        nullable=True,
    ),
    Column(
        "statement_descriptor_prefix",
        String,
        comment="The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion",
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
__all__ = ["account_card_payments_settings.json"]
