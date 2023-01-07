from sqlalchemy import Column, Integer


class Setup_Intent_Payment_Method_Options(Base):
    __tablename__ = "setup_intent_payment_method_options"
    acss_debit = Column(
        setup_intent_payment_method_options_acss_debit,
        ForeignKey("setup_intent_payment_method_options_acss_debit"),
        nullable=True,
    )
    blik = Column(
        setup_intent_payment_method_options_blik,
        ForeignKey("setup_intent_payment_method_options_blik"),
        nullable=True,
    )
    card = Column(
        setup_intent_payment_method_options_card,
        ForeignKey("setup_intent_payment_method_options_card"),
        nullable=True,
    )
    link = Column(
        setup_intent_payment_method_options_link,
        ForeignKey("setup_intent_payment_method_options_link"),
        nullable=True,
    )
    sepa_debit = Column(
        setup_intent_payment_method_options_sepa_debit,
        ForeignKey("setup_intent_payment_method_options_sepa_debit"),
        nullable=True,
    )
    us_bank_account = Column(
        setup_intent_payment_method_options_us_bank_account,
        ForeignKey("setup_intent_payment_method_options_us_bank_account"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Intent_Payment_Method_Options(acss_debit={acss_debit!r}, blik={blik!r}, card={card!r}, link={link!r}, sepa_debit={sepa_debit!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            blik=self.blik,
            card=self.card,
            link=self.link,
            sepa_debit=self.sepa_debit,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options"]
