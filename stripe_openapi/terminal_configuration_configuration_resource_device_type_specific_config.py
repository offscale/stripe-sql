from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig(Base):
    __tablename__ = (
        "terminal_configuration_configuration_resource_device_type_specific_config"
    )
    splashscreen = Column(
        File,
        ForeignKey("File"),
        comment="A File ID representing an image you would like displayed on the reader",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig(splashscreen={splashscreen!r}, id={id!r})".format(
            splashscreen=self.splashscreen, id=self.id
        )


__all__ = ["terminal_configuration_configuration_resource_device_type_specific_config"]
