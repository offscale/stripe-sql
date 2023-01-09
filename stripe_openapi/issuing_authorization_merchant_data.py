from sqlalchemy import Column, String

from . import Base


class IssuingAuthorizationMerchantData(Base):
    __tablename__ = "issuing_authorization_merchant_data"
    category = Column(
        String,
        comment="A categorization of the seller's type of business. See our [merchant categories guide](https://stripe.com/docs/issuing/merchant-categories) for a list of possible values",
    )
    category_code = Column(
        String, comment="The merchant category code for the seller’s business"
    )
    city = Column(String, comment="City where the seller is located", nullable=True)
    country = Column(
        String, comment="Country where the seller is located", nullable=True
    )
    name = Column(String, comment="Name of the seller", nullable=True)
    network_id = Column(
        String,
        comment="Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant",
        primary_key=True,
    )
    postal_code = Column(
        String, comment="Postal code where the seller is located", nullable=True
    )
    state = Column(String, comment="State where the seller is located", nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingAuthorizationMerchantData(category={category!r}, category_code={category_code!r}, city={city!r}, country={country!r}, name={name!r}, network_id={network_id!r}, postal_code={postal_code!r}, state={state!r})".format(
            category=self.category,
            category_code=self.category_code,
            city=self.city,
            country=self.country,
            name=self.name,
            network_id=self.network_id,
            postal_code=self.postal_code,
            state=self.state,
        )


__all__ = ["issuing_authorization_merchant_data"]
