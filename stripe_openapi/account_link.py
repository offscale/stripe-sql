from sqlalchemy import Column, Identity, Integer, String

from . import Base


class AccountLink(Base):
    """
    Account Links are the means by which a Connect platform grants a connected account permission to access

    Stripe-hosted applications, such as Connect Onboarding.

    Related guide: [Connect Onboarding](https://stripe.com/docs/connect/connect-onboarding).

    """

    __tablename__ = "account_link"
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    expires_at = Column(
        Integer, comment="The timestamp at which this account link will expire"
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    url = Column(String, comment="The URL for the account link")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountLink(created={created!r}, expires_at={expires_at!r}, object={object!r}, url={url!r}, id={id!r})".format(
            created=self.created,
            expires_at=self.expires_at,
            object=self.object,
            url=self.url,
            id=self.id,
        )


__all__ = ["account_link"]
