from sqlalchemy import Boolean, Column, Integer, String


class File_Link(Base):
    """
    To share the contents of a `File` object with non-Stripe users, you can

    create a `FileLink`. `FileLink`s contain a URL that can be used to
    retrieve the contents of the file without authentication.

    """

    __tablename__ = "file_link"
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    expired = Column(Boolean, comment="Whether this link is already expired")
    expires_at = Column(
        Integer, comment="Time at which the link expires", nullable=True
    )
    file = Column(File, comment="The file object this link points to")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    url = Column(
        String,
        comment="The publicly accessible URL to download the file",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "File_Link(created={created!r}, expired={expired!r}, expires_at={expires_at!r}, file={file!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, url={url!r})".format(
            created=self.created,
            expired=self.expired,
            expires_at=self.expires_at,
            file=self.file,
            id=self.id,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            url=self.url,
        )


__all__ = ["file_link"]
