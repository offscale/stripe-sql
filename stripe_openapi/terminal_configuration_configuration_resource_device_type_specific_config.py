from sqlalchemy import Column, Integer


class Terminal_Configuration_Configuration_Resource_Device_Type_Specific_Config(Base):
    __tablename__ = (
        "terminal_configuration_configuration_resource_device_type_specific_config"
    )
    splashscreen = Column(
        File,
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
        return "Terminal_Configuration_Configuration_Resource_Device_Type_Specific_Config(splashscreen={splashscreen!r}, id={id!r})".format(
            splashscreen=self.splashscreen, id=self.id
        )


__all__ = ["terminal_configuration_configuration_resource_device_type_specific_config"]
