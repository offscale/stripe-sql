from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodFpxJson = Table(
    "payment_method_fpxjson",
    metadata,
    Column(
        "account_holder_type",
        String,
        comment="Account holder type, if provided. Can be one of `individual` or `company`",
        nullable=True,
    ),
    Column(
        "bank",
        String,
        comment="The customer's bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_fpx.json"]
