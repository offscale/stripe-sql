from sqlalchemy import Column, String

from . import Base


class PaymentMethodDetailsP24(Base):
    __tablename__ = "payment_method_details_p24"
    bank = Column(
        String,
        comment="The customer's bank. Can be one of `ing`, `citi_handlowy`, `tmobile_usbugi_bankowe`, `plus_bank`, `etransfer_pocztowy24`, `banki_spbdzielcze`, `bank_nowy_bfg_sa`, `getin_bank`, `blik`, `noble_pay`, `ideabank`, `envelobank`, `santander_przelew24`, `nest_przelew`, `mbank_mtransfer`, `inteligo`, `pbac_z_ipko`, `bnp_paribas`, `credit_agricole`, `toyota_bank`, `bank_pekao_sa`, `volkswagen_bank`, `bank_millennium`, `alior_bank`, or `boz`",
        nullable=True,
    )
    reference = Column(
        String, comment="Unique reference for this Przelewy24 payment", nullable=True
    )
    verified_name = Column(
        String,
        comment="Owner's verified full name. Values are verified or provided by Przelewy24 directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated.\nPrzelewy24 rarely provides this information so the attribute is usually empty",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsP24(bank={bank!r}, reference={reference!r}, verified_name={verified_name!r})".format(
            bank=self.bank, reference=self.reference, verified_name=self.verified_name
        )


__all__ = ["payment_method_details_p24"]
