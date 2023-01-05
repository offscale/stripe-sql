from sqlalchemy import Column, Integer, String


class Login_Link(Base):
    __tablename__ = "login_link"
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    url = Column(String, comment="The URL for the login link")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Login_Link(created={created!r}, object={object!r}, url={url!r}, id={id!r})".format(
            created=self.created, object=self.object, url=self.url, id=self.id
        )


__all__ = ["login_link"]
