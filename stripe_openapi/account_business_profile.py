from sqlalchemy import Column, Integer, String


class Account_Business_Profile(Base):
    __tablename__ = "account_business_profile"
    mcc = Column(
        String,
        comment="[The merchant category code for the account](https://stripe.com/docs/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide",
        nullable=True,
    )
    name = Column(String, comment="The customer-facing business name", nullable=True)
    product_description = Column(
        String,
        comment="Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes",
        nullable=True,
    )
    support_address = Column(
        Address,
        comment="A publicly available mailing address for sending support issues to",
        nullable=True,
    )
    support_email = Column(
        String,
        comment="A publicly available email address for sending support issues to",
        nullable=True,
    )
    support_phone = Column(
        String,
        comment="A publicly available phone number to call with support issues",
        nullable=True,
    )
    support_url = Column(
        String,
        comment="A publicly available website for handling support issues",
        nullable=True,
    )
    url = Column(
        String, comment="The business's publicly available website", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Business_Profile(mcc={mcc!r}, name={name!r}, product_description={product_description!r}, support_address={support_address!r}, support_email={support_email!r}, support_phone={support_phone!r}, support_url={support_url!r}, url={url!r}, id={id!r})".format(
            mcc=self.mcc,
            name=self.name,
            product_description=self.product_description,
            support_address=self.support_address,
            support_email=self.support_email,
            support_phone=self.support_phone,
            support_url=self.support_url,
            url=self.url,
            id=self.id,
        )


__all__ = ["account_business_profile"]
