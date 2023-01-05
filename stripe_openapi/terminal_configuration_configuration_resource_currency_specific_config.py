from sqlalchemy import Column, Integer


class Terminal_Configuration_Configuration_Resource_Currency_Specific_Config(Base):
    __tablename__ = (
        "terminal_configuration_configuration_resource_currency_specific_config"
    )
    fixed_amounts = Column(
        list, comment="Fixed amounts displayed when collecting a tip", nullable=True
    )
    percentages = Column(
        list, comment="Percentages displayed when collecting a tip", nullable=True
    )
    smart_tip_threshold = Column(
        Integer,
        comment="Below this amount, fixed amounts will be displayed; above it, percentages will be displayed",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Terminal_Configuration_Configuration_Resource_Currency_Specific_Config(fixed_amounts={fixed_amounts!r}, percentages={percentages!r}, smart_tip_threshold={smart_tip_threshold!r}, id={id!r})".format(
            fixed_amounts=self.fixed_amounts,
            percentages=self.percentages,
            smart_tip_threshold=self.smart_tip_threshold,
            id=self.id,
        )


__all__ = ["terminal_configuration_configuration_resource_currency_specific_config"]
