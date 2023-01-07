from sqlalchemy import Column, Integer, String


class Account_Branding_Settings(Base):
    __tablename__ = "account_branding_settings"
    icon = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px",
        nullable=True,
    )
    logo = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px",
        nullable=True,
    )
    primary_color = Column(
        String,
        comment="A CSS hex color value representing the primary branding color for this account",
        nullable=True,
    )
    secondary_color = Column(
        String,
        comment="A CSS hex color value representing the secondary branding color for this account",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Branding_Settings(icon={icon!r}, logo={logo!r}, primary_color={primary_color!r}, secondary_color={secondary_color!r}, id={id!r})".format(
            icon=self.icon,
            logo=self.logo,
            primary_color=self.primary_color,
            secondary_color=self.secondary_color,
            id=self.id,
        )


__all__ = ["account_branding_settings"]
