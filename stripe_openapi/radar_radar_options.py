from sqlalchemy import Column, Integer, String


class Radar_Radar_Options(Base):
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """

    __tablename__ = "radar_radar_options"
    session = Column(
        String,
        comment="A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Radar_Radar_Options(session={session!r}, id={id!r})".format(
            session=self.session, id=self.id
        )


__all__ = ["radar_radar_options"]
