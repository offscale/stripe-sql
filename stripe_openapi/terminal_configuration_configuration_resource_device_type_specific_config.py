from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.file import File

from . import metadata

TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfigJson = Table(
    "terminal_configuration_configuration_resource_device_type_specific_configjson",
    metadata,
    Column(
        "splashscreen",
        File,
        ForeignKey("File"),
        comment="A File ID representing an image you would like displayed on the reader",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "terminal_configuration_configuration_resource_device_type_specific_config.json"
]
