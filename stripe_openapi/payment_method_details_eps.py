from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsEpsJson = Table(
    "payment_method_details_epsjson",
    metadata,
    Column(
        "bank",
        String,
        comment="The customer's bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`",
        nullable=True,
    ),
    Column(
        "verified_name",
        String,
        comment="Owner's verified full name. Values are verified or provided by EPS directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated.\nEPS rarely provides this information so the attribute is usually empty",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["payment_method_details_eps.json"]
