from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class SetupIntentPaymentMethodOptions(Base):
    __tablename__ = "setup_intent_payment_method_options"
    acss_debit = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_acss_debit.id"),
        nullable=True,
    )
    blik = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_blik.id"),
        nullable=True,
    )
    card = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_card.id"),
        nullable=True,
    )
    link = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_link.id"),
        nullable=True,
    )
    sepa_debit = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_sepa_debit.id"),
        nullable=True,
    )
    us_bank_account = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_us_bank_account.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentPaymentMethodOptions(acss_debit={acss_debit!r}, blik={blik!r}, card={card!r}, link={link!r}, sepa_debit={sepa_debit!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            acss_debit=self.acss_debit,
            blik=self.blik,
            card=self.card,
            link=self.link,
            sepa_debit=self.sepa_debit,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options"]
