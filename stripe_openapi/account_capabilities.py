from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AccountCapabilitiesJson = Table(
    "account_capabilitiesjson",
    metadata,
    Column(
        "acss_debit_payments",
        String,
        comment="The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges",
        nullable=True,
    ),
    Column(
        "affirm_payments",
        String,
        comment="The status of the Affirm capability of the account, or whether the account can directly process Affirm charges",
        nullable=True,
    ),
    Column(
        "afterpay_clearpay_payments",
        String,
        comment="The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges",
        nullable=True,
    ),
    Column(
        "au_becs_debit_payments",
        String,
        comment="The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges",
        nullable=True,
    ),
    Column(
        "bacs_debit_payments",
        String,
        comment="The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges",
        nullable=True,
    ),
    Column(
        "bancontact_payments",
        String,
        comment="The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges",
        nullable=True,
    ),
    Column(
        "bank_transfer_payments",
        String,
        comment="The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges",
        nullable=True,
    ),
    Column(
        "blik_payments",
        String,
        comment="The status of the blik payments capability of the account, or whether the account can directly process blik charges",
        nullable=True,
    ),
    Column(
        "boleto_payments",
        String,
        comment="The status of the boleto payments capability of the account, or whether the account can directly process boleto charges",
        nullable=True,
    ),
    Column(
        "card_issuing",
        String,
        comment="The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards",
        nullable=True,
    ),
    Column(
        "card_payments",
        String,
        comment="The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges",
        nullable=True,
    ),
    Column(
        "cartes_bancaires_payments",
        String,
        comment="The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency",
        nullable=True,
    ),
    Column(
        "cashapp_payments",
        String,
        comment="The status of the Cash App Pay capability of the account, or whether the account can directly process Cash App Pay payments",
        nullable=True,
    ),
    Column(
        "eps_payments",
        String,
        comment="The status of the EPS payments capability of the account, or whether the account can directly process EPS charges",
        nullable=True,
    ),
    Column(
        "fpx_payments",
        String,
        comment="The status of the FPX payments capability of the account, or whether the account can directly process FPX charges",
        nullable=True,
    ),
    Column(
        "giropay_payments",
        String,
        comment="The status of the giropay payments capability of the account, or whether the account can directly process giropay charges",
        nullable=True,
    ),
    Column(
        "grabpay_payments",
        String,
        comment="The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges",
        nullable=True,
    ),
    Column(
        "ideal_payments",
        String,
        comment="The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges",
        nullable=True,
    ),
    Column(
        "india_international_payments",
        String,
        comment="The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India",
        nullable=True,
    ),
    Column(
        "jcb_payments",
        String,
        comment="The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency",
        nullable=True,
    ),
    Column(
        "klarna_payments",
        String,
        comment="The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges",
        nullable=True,
    ),
    Column(
        "konbini_payments",
        String,
        comment="The status of the konbini payments capability of the account, or whether the account can directly process konbini charges",
        nullable=True,
    ),
    Column(
        "legacy_payments",
        String,
        comment="The status of the legacy payments capability of the account",
        nullable=True,
    ),
    Column(
        "link_payments",
        String,
        comment="The status of the link_payments capability of the account, or whether the account can directly process Link charges",
        nullable=True,
    ),
    Column(
        "oxxo_payments",
        String,
        comment="The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges",
        nullable=True,
    ),
    Column(
        "p24_payments",
        String,
        comment="The status of the P24 payments capability of the account, or whether the account can directly process P24 charges",
        nullable=True,
    ),
    Column(
        "paynow_payments",
        String,
        comment="The status of the paynow payments capability of the account, or whether the account can directly process paynow charges",
        nullable=True,
    ),
    Column(
        "promptpay_payments",
        String,
        comment="The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges",
        nullable=True,
    ),
    Column(
        "sepa_debit_payments",
        String,
        comment="The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges",
        nullable=True,
    ),
    Column(
        "sofort_payments",
        String,
        comment="The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges",
        nullable=True,
    ),
    Column(
        "tax_reporting_us_1099_k",
        String,
        comment="The status of the tax reporting 1099-K (US) capability of the account",
        nullable=True,
    ),
    Column(
        "tax_reporting_us_1099_misc",
        String,
        comment="The status of the tax reporting 1099-MISC (US) capability of the account",
        nullable=True,
    ),
    Column(
        "transfers",
        String,
        comment="The status of the transfers capability of the account, or whether your platform can transfer funds to the account",
        nullable=True,
    ),
    Column(
        "treasury",
        String,
        comment="The status of the banking capability, or whether the account can have bank accounts",
        nullable=True,
    ),
    Column(
        "us_bank_account_ach_payments",
        String,
        comment="The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_capabilities.json"]
