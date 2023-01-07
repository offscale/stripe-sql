from sqlalchemy import Column, Integer, String


class Setup_Attempt_Payment_Method_Details(Base):
    __tablename__ = "setup_attempt_payment_method_details"
    acss_debit = Column(
        setup_attempt_payment_method_details_acss_debit,
        ForeignKey("setup_attempt_payment_method_details_acss_debit"),
        nullable=True,
    )
    au_becs_debit = Column(
        setup_attempt_payment_method_details_au_becs_debit,
        ForeignKey("setup_attempt_payment_method_details_au_becs_debit"),
        nullable=True,
    )
    bacs_debit = Column(
        setup_attempt_payment_method_details_bacs_debit,
        ForeignKey("setup_attempt_payment_method_details_bacs_debit"),
        nullable=True,
    )
    bancontact = Column(
        setup_attempt_payment_method_details_bancontact,
        ForeignKey("setup_attempt_payment_method_details_bancontact"),
        nullable=True,
    )
    blik = Column(
        setup_attempt_payment_method_details_blik,
        ForeignKey("setup_attempt_payment_method_details_blik"),
        nullable=True,
    )
    boleto = Column(
        setup_attempt_payment_method_details_boleto,
        ForeignKey("setup_attempt_payment_method_details_boleto"),
        nullable=True,
    )
    card = Column(
        setup_attempt_payment_method_details_card,
        ForeignKey("setup_attempt_payment_method_details_card"),
        nullable=True,
    )
    card_present = Column(
        setup_attempt_payment_method_details_card_present,
        ForeignKey("setup_attempt_payment_method_details_card_present"),
        nullable=True,
    )
    ideal = Column(
        setup_attempt_payment_method_details_ideal,
        ForeignKey("setup_attempt_payment_method_details_ideal"),
        nullable=True,
    )
    klarna = Column(
        setup_attempt_payment_method_details_klarna,
        ForeignKey("setup_attempt_payment_method_details_klarna"),
        nullable=True,
    )
    link = Column(
        setup_attempt_payment_method_details_link,
        ForeignKey("setup_attempt_payment_method_details_link"),
        nullable=True,
    )
    sepa_debit = Column(
        setup_attempt_payment_method_details_sepa_debit,
        ForeignKey("setup_attempt_payment_method_details_sepa_debit"),
        nullable=True,
    )
    sofort = Column(
        setup_attempt_payment_method_details_sofort,
        ForeignKey("setup_attempt_payment_method_details_sofort"),
        nullable=True,
    )
    type = Column(
        String,
        comment="The type of the payment method used in the SetupIntent (e.g., `card`). An additional hash is included on `payment_method_details` with a name matching this value. It contains confirmation-specific information for the payment method",
    )
    us_bank_account = Column(
        setup_attempt_payment_method_details_us_bank_account,
        ForeignKey("setup_attempt_payment_method_details_us_bank_account"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Attempt_Payment_Method_Details(acss_debit={acss_debit!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, bancontact={bancontact!r}, blik={blik!r}, boleto={boleto!r}, card={card!r}, card_present={card_present!r}, ideal={ideal!r}, klarna={klarna!r}, link={link!r}, sepa_debit={sepa_debit!r}, sofort={sofort!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
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
