from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodOptionsCardMandateOptions.Json = Table(
    "payment_method_options_card_mandate_options.json",
    metadata,
    Column("amount", Integer, comment="Amount to be charged for future payments"),
    Column(
        "amount_type",
        String,
        comment="One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param",
    ),
    Column(
        "description",
        String,
        comment="A description of the mandate or subscription that is meant to be displayed to the customer",
        nullable=True,
    ),
    Column(
        "end_date",
        Integer,
        comment="End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date",
        nullable=True,
    ),
    Column(
        "interval",
        String,
        comment="Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`",
    ),
    Column(
        "interval_count",
        Integer,
        comment="The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`",
        nullable=True,
    ),
    Column(
        "reference", String, comment="Unique identifier for the mandate or subscription"
    ),
    Column(
        "start_date",
        Integer,
        comment="Start date of the mandate or subscription. Start date should not be lesser than yesterday",
    ),
    Column(
        "supported_types",
        ARRAY(String),
        comment="Specifies the type of mandates supported. Possible values are `india`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_card_mandate_options.json"]
