from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

FundingInstructionsJson = Table(
    "funding_instructionsjson",
    metadata,
    Column(
        "bank_transfer",
        FundingInstructionsBankTransfer,
        ForeignKey("FundingInstructionsBankTransfer"),
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "funding_type",
        String,
        comment="The `funding_type` of the returned instructions",
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["funding_instructions.json"]
