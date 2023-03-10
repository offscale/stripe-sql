from sqlalchemy import ARRAY, Column, Identity, Integer, String, list

from . import Base


class IssuingCardholderAuthorizationControls(Base):
    __tablename__ = "issuing_cardholder_authorization_controls"
    allowed_categories = Column(
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`",
        nullable=True,
    )
    blocked_categories = Column(
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`",
        nullable=True,
    )
    spending_limits = Column(
        list,
        comment="Limit spending with amount-based rules that apply across this cardholder's cards",
        nullable=True,
    )
    spending_limits_currency = Column(
        String,
        comment="Currency of the amounts within `spending_limits`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderAuthorizationControls(allowed_categories={allowed_categories!r}, blocked_categories={blocked_categories!r}, spending_limits={spending_limits!r}, spending_limits_currency={spending_limits_currency!r}, id={id!r})".format(
            allowed_categories=self.allowed_categories,
            blocked_categories=self.blocked_categories,
            spending_limits=self.spending_limits,
            spending_limits_currency=self.spending_limits_currency,
            id=self.id,
        )


__all__ = ["issuing_cardholder_authorization_controls"]
