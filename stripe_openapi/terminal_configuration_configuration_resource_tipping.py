from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TerminalConfigurationConfigurationResourceTippingJson = Table(
    "terminal_configuration_configuration_resource_tippingjson",
    metadata,
    Column(
        "aud",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "cad",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "chf",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "czk",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "dkk",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "eur",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "gbp",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "hkd",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "myr",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "nok",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "nzd",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "sek",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "sgd",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column(
        "usd",
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
        ForeignKey("TerminalConfigurationConfigurationResourceCurrencySpecificConfig"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_configuration_configuration_resource_tipping.json"]
