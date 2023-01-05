from sqlalchemy import Column, String


class Country_Spec(Base):
    """
    Stripe needs to collect certain pieces of information about each account

    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](/docs/connect/required-verification-information).

    """

    __tablename__ = "country_spec"
    default_currency = Column(
        String,
        comment="The default currency for this country. This applies to both payment methods and bank accounts",
    )
    id = Column(
        String,
        comment="Unique identifier for the object. Represented as the ISO country code for this country",
        primary_key=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    supported_bank_account_currencies = Column(
        JSON,
        comment="Currencies that can be accepted in the specific country (for transfers)",
    )
    supported_payment_currencies = Column(
        ARRAY(String),
        comment="Currencies that can be accepted in the specified country (for payments)",
    )
    supported_payment_methods = Column(
        ARRAY(String),
        comment="Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges)",
    )
    supported_transfer_countries = Column(
        ARRAY(String),
        comment="Countries that can accept transfers from the specified country",
    )
    verification_fields = Column(CountrySpecVerificationFields)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Country_Spec(default_currency={default_currency!r}, id={id!r}, object={object!r}, supported_bank_account_currencies={supported_bank_account_currencies!r}, supported_payment_currencies={supported_payment_currencies!r}, supported_payment_methods={supported_payment_methods!r}, supported_transfer_countries={supported_transfer_countries!r}, verification_fields={verification_fields!r})".format(
            default_currency=self.default_currency,
            id=self.id,
            object=self.object,
            supported_bank_account_currencies=self.supported_bank_account_currencies,
            supported_payment_currencies=self.supported_payment_currencies,
            supported_payment_methods=self.supported_payment_methods,
            supported_transfer_countries=self.supported_transfer_countries,
            verification_fields=self.verification_fields,
        )


__all__ = ["country_spec"]
