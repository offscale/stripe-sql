from sqlalchemy import ARRAY, JSON, Column, ForeignKey, String, Table

from . import metadata

CountrySpecJson = Table(
    "country_specjson",
    metadata,
    Column(
        "default_currency",
        String,
        comment="The default currency for this country. This applies to both payment methods and bank accounts",
    ),
    Column(
        "id",
        String,
        comment="Unique identifier for the object. Represented as the ISO country code for this country",
        primary_key=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "supported_bank_account_currencies",
        JSON,
        comment="Currencies that can be accepted in the specific country (for transfers)",
    ),
    Column(
        "supported_payment_currencies",
        ARRAY(String),
        comment="Currencies that can be accepted in the specified country (for payments)",
    ),
    Column(
        "supported_payment_methods",
        ARRAY(String),
        comment="Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges)",
    ),
    Column(
        "supported_transfer_countries",
        ARRAY(String),
        comment="Countries that can accept transfers from the specified country",
    ),
    Column(
        "verification_fields",
        CountrySpecVerificationFields,
        ForeignKey("CountrySpecVerificationFields"),
    ),
)
__all__ = ["country_spec.json"]
