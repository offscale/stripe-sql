from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodOptionsCustomerBalanceEuBankAccountJson = Table(
    "payment_method_options_customer_balance_eu_bank_accountjson",
    metadata,
    Column(
        "country",
        String,
        comment="The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_customer_balance_eu_bank_account.json"]
