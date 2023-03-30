from sqlalchemy import Column, Identity, Integer, Table, list

from . import metadata

TerminalConfigurationConfigurationResourceCurrencySpecificConfig.Json = Table(
    "terminal_configuration_configuration_resource_currency_specific_config.json",
    metadata,
    Column(
        "fixed_amounts",
        list,
        comment="Fixed amounts displayed when collecting a tip",
        nullable=True,
    ),
    Column(
        "percentages",
        list,
        comment="Percentages displayed when collecting a tip",
        nullable=True,
    ),
    Column(
        "smart_tip_threshold",
        Integer,
        comment="Below this amount, fixed amounts will be displayed; above it, percentages will be displayed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "terminal_configuration_configuration_resource_currency_specific_config.json"
]
