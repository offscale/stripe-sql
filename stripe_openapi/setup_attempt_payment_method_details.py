from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class SetupAttemptPaymentMethodDetails(Base):
    __tablename__ = "setup_attempt_payment_method_details"
    acss_debit = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_acss_debit.id"),
        nullable=True,
    )
    au_becs_debit = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_au_becs_debit.id"),
        nullable=True,
    )
    bacs_debit = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_bacs_debit.id"),
        nullable=True,
    )
    bancontact = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_bancontact.id"),
        nullable=True,
    )
    blik = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_blik.id"),
        nullable=True,
    )
    boleto = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_boleto.id"),
        nullable=True,
    )
    card = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_card.id"),
        nullable=True,
    )
    card_present = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_card_present.id"),
        nullable=True,
    )
    ideal = Column(
        String,
        ForeignKey("setup_attempt_payment_method_details_ideal.verified_name"),
        nullable=True,
    )
    klarna = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_klarna.id"),
        nullable=True,
    )
    link = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_link.id"),
        nullable=True,
    )
    sepa_debit = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_sepa_debit.id"),
        nullable=True,
    )
    sofort = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_sofort.id"),
        nullable=True,
    )
    type = Column(
        String,
        comment="The type of the payment method used in the SetupIntent (e.g., `card`). An additional hash is included on `payment_method_details` with a name matching this value. It contains confirmation-specific information for the payment method",
    )
    us_bank_account = Column(
        Integer,
        ForeignKey("setup_attempt_payment_method_details_us_bank_account.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupAttemptPaymentMethodDetails(acss_debit={acss_debit!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, ideal={ideal!r}, klarna={klarna!r}, link={link!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            au_becs_debit=self.au_becs_debit,
            bacs_debit=self.bacs_debit,
            bancontact=self.bancontact,
            blik=self.blik,
            boleto=self.boleto,
            card=self.card,
            card_present=self.card_present,
            ideal=self.ideal,
            klarna=self.klarna,
            link=self.link,
            sepa_debit=self.sepa_debit,
            sofort=self.sofort,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["setup_attempt_payment_method_details"]
