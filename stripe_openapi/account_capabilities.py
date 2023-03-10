from sqlalchemy import Column, Identity, Integer, String

from . import Base


class AccountCapabilities(Base):
    __tablename__ = "account_capabilities"
    acss_debit_payments = Column(
        String,
        comment="The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges",
        nullable=True,
    )
    affirm_payments = Column(
        String,
        comment="The status of the Affirm capability of the account, or whether the account can directly process Affirm charges",
        nullable=True,
    )
    afterpay_clearpay_payments = Column(
        String,
        comment="The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges",
        nullable=True,
    )
    au_becs_debit_payments = Column(
        String,
        comment="The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges",
        nullable=True,
    )
    bacs_debit_payments = Column(
        String,
        comment="The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges",
        nullable=True,
    )
    bancontact_payments = Column(
        String,
        comment="The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges",
        nullable=True,
    )
    bank_transfer_payments = Column(
        String,
        comment="The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges",
        nullable=True,
    )
    blik_payments = Column(
        String,
        comment="The status of the blik payments capability of the account, or whether the account can directly process blik charges",
        nullable=True,
    )
    boleto_payments = Column(
        String,
        comment="The status of the boleto payments capability of the account, or whether the account can directly process boleto charges",
        nullable=True,
    )
    card_issuing = Column(
        String,
        comment="The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards",
        nullable=True,
    )
    card_payments = Column(
        String,
        comment="The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges",
        nullable=True,
    )
    cartes_bancaires_payments = Column(
        String,
        comment="The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency",
        nullable=True,
    )
    eps_payments = Column(
        String,
        comment="The status of the EPS payments capability of the account, or whether the account can directly process EPS charges",
        nullable=True,
    )
    fpx_payments = Column(
        String,
        comment="The status of the FPX payments capability of the account, or whether the account can directly process FPX charges",
        nullable=True,
    )
    giropay_payments = Column(
        String,
        comment="The status of the giropay payments capability of the account, or whether the account can directly process giropay charges",
        nullable=True,
    )
    grabpay_payments = Column(
        String,
        comment="The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges",
        nullable=True,
    )
    ideal_payments = Column(
        String,
        comment="The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges",
        nullable=True,
    )
    india_international_payments = Column(
        String,
        comment="The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India",
        nullable=True,
    )
    jcb_payments = Column(
        String,
        comment="The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency",
        nullable=True,
    )
    klarna_payments = Column(
        String,
        comment="The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges",
        nullable=True,
    )
    konbini_payments = Column(
        String,
        comment="The status of the konbini payments capability of the account, or whether the account can directly process konbini charges",
        nullable=True,
    )
    legacy_payments = Column(
        String,
        comment="The status of the legacy payments capability of the account",
        nullable=True,
    )
    link_payments = Column(
        String,
        comment="The status of the link_payments capability of the account, or whether the account can directly process Link charges",
        nullable=True,
    )
    oxxo_payments = Column(
        String,
        comment="The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges",
        nullable=True,
    )
    p24_payments = Column(
        String,
        comment="The status of the P24 payments capability of the account, or whether the account can directly process P24 charges",
        nullable=True,
    )
    paynow_payments = Column(
        String,
        comment="The status of the paynow payments capability of the account, or whether the account can directly process paynow charges",
        nullable=True,
    )
    promptpay_payments = Column(
        String,
        comment="The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges",
        nullable=True,
    )
    sepa_debit_payments = Column(
        String,
        comment="The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges",
        nullable=True,
    )
    sofort_payments = Column(
        String,
        comment="The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges",
        nullable=True,
    )
    tax_reporting_us_1099_k = Column(
        String,
        comment="The status of the tax reporting 1099-K (US) capability of the account",
        nullable=True,
    )
    tax_reporting_us_1099_misc = Column(
        String,
        comment="The status of the tax reporting 1099-MISC (US) capability of the account",
        nullable=True,
    )
    transfers = Column(
        String,
        comment="The status of the transfers capability of the account, or whether your platform can transfer funds to the account",
        nullable=True,
    )
    treasury = Column(
        String,
        comment="The status of the banking capability, or whether the account can have bank accounts",
        nullable=True,
    )
    us_bank_account_ach_payments = Column(
        String,
        comment="The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountCapabilities(acss_debit_payments={acss_debit_payments!r}, affirm_payments={affirm_payments!r}, afterpay_clearpay_payments={afterpay_clearpay_payments!r}, au_becs_debit_payments={au_becs_debit_payments!r}, bacs_debit_payments={bacs_debit_payments!r}, bancontact_payments={bancontact_payments!r}, bank_transfer_payments={bank_transfer_payments!r}, blik_payments={blik_payments!r}, boleto_payments={boleto_payments!r}, card_issuing={card_issuing!r}, card_payments={card_payments!r}, cartes_bancaires_payments={cartes_bancaires_payments!r}, eps_payments={eps_payments!r}, fpx_payments={fpx_payments!r}, giropay_payments={giropay_payments!r}, grabpay_payments={grabpay_payments!r}, ideal_payments={ideal_payments!r}, india_international_payments={india_international_payments!r}, jcb_payments={jcb_payments!r}, klarna_payments={klarna_payments!r}, konbini_payments={konbini_payments!r}, legacy_payments={legacy_payments!r}, link_payments={link_payments!r}, oxxo_payments={oxxo_payments!r}, p24_payments={p24_payments!r}, paynow_payments={paynow_payments!r}, promptpay_payments={promptpay_payments!r}, sepa_debit_payments={sepa_debit_payments!r}, sofort_payments={sofort_payments!r}, tax_reporting_us_1099_k={tax_reporting_us_1099_k!r}, tax_reporting_us_1099_misc={tax_reporting_us_1099_misc!r}, transfers={transfers!r}, treasury={treasury!r}, us_bank_account_ach_payments={us_bank_account_ach_payments!r}, id={id!r})".format(
            acss_debit_payments=self.acss_debit_payments,
            affirm_payments=self.affirm_payments,
            afterpay_clearpay_payments=self.afterpay_clearpay_payments,
            au_becs_debit_payments=self.au_becs_debit_payments,
            bacs_debit_payments=self.bacs_debit_payments,
            bancontact_payments=self.bancontact_payments,
            bank_transfer_payments=self.bank_transfer_payments,
            blik_payments=self.blik_payments,
            boleto_payments=self.boleto_payments,
            card_issuing=self.card_issuing,
            card_payments=self.card_payments,
            cartes_bancaires_payments=self.cartes_bancaires_payments,
            eps_payments=self.eps_payments,
            fpx_payments=self.fpx_payments,
            giropay_payments=self.giropay_payments,
            grabpay_payments=self.grabpay_payments,
            ideal_payments=self.ideal_payments,
            india_international_payments=self.india_international_payments,
            jcb_payments=self.jcb_payments,
            klarna_payments=self.klarna_payments,
            konbini_payments=self.konbini_payments,
            legacy_payments=self.legacy_payments,
            link_payments=self.link_payments,
            oxxo_payments=self.oxxo_payments,
            p24_payments=self.p24_payments,
            paynow_payments=self.paynow_payments,
            promptpay_payments=self.promptpay_payments,
            sepa_debit_payments=self.sepa_debit_payments,
            sofort_payments=self.sofort_payments,
            tax_reporting_us_1099_k=self.tax_reporting_us_1099_k,
            tax_reporting_us_1099_misc=self.tax_reporting_us_1099_misc,
            transfers=self.transfers,
            treasury=self.treasury,
            us_bank_account_ach_payments=self.us_bank_account_ach_payments,
            id=self.id,
        )


__all__ = ["account_capabilities"]
