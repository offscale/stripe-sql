from sqlalchemy import Column, ForeignKey, String

from . import Base


class PaymentMethodDetailsIdeal(Base):
    __tablename__ = "payment_method_details_ideal"
    bank = Column(
        String,
        comment="The customer's bank. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, or `van_lanschot`",
        nullable=True,
    )
    bic = Column(
        String, comment="The Bank Identifier Code of the customer's bank", nullable=True
    )
    generated_sepa_debit = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge",
        nullable=True,
    )
    generated_sepa_debit_mandate = Column(
        Mandate,
        ForeignKey("Mandate"),
        comment="The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge",
        nullable=True,
    )
    iban_last4 = Column(
        String, comment="Last four characters of the IBAN", nullable=True
    )
    verified_name = Column(
        String,
        comment="Owner's verified full name. Values are verified or provided by iDEAL directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsIdeal(bank={bank!r}, bic={bic!r}, generated_sepa_debit={generated_sepa_debit!r}, generated_sepa_debit_mandate={generated_sepa_debit_mandate!r}, iban_last4={iban_last4!r}, verified_name={verified_name!r})".format(
            bank=self.bank,
            bic=self.bic,
            generated_sepa_debit=self.generated_sepa_debit,
            generated_sepa_debit_mandate=self.generated_sepa_debit_mandate,
            iban_last4=self.iban_last4,
            verified_name=self.verified_name,
        )


__all__ = ["payment_method_details_ideal"]
