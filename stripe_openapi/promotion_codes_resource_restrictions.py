from sqlalchemy import JSON, Boolean, Column, Identity, Integer, String

from . import Base


class PromotionCodesResourceRestrictions(Base):
    __tablename__ = "promotion_codes_resource_restrictions"
    currency_options = Column(
        JSON,
        comment="Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    )
    first_time_transaction = Column(
        Boolean,
        comment="A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices",
    )
    minimum_amount = Column(
        Integer,
        comment="Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work)",
        nullable=True,
    )
    minimum_amount_currency = Column(
        String,
        comment="Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PromotionCodesResourceRestrictions(currency_options={currency_options!r}, first_time_transaction={first_time_transaction!r}, minimum_amount={minimum_amount!r}, minimum_amount_currency={minimum_amount_currency!r}, id={id!r})".format(
            currency_options=self.currency_options,
            first_time_transaction=self.first_time_transaction,
            minimum_amount=self.minimum_amount,
            minimum_amount_currency=self.minimum_amount_currency,
            id=self.id,
        )


__all__ = ["promotion_codes_resource_restrictions"]
