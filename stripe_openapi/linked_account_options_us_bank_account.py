from sqlalchemy import Column, Integer, String


class Linked_Account_Options_Us_Bank_Account(Base):
    __tablename__ = "linked_account_options_us_bank_account"
    permissions = Column(
        ARRAY(String),
        comment="The list of permissions to request. The `payment_method` permission must be included",
        nullable=True,
    )
    return_url = Column(
        String,
        comment="For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Linked_Account_Options_Us_Bank_Account(permissions={permissions!r}, return_url={return_url!r}, id={id!r})".format(
            permissions=self.permissions, return_url=self.return_url, id=self.id
        )


__all__ = ["linked_account_options_us_bank_account"]
