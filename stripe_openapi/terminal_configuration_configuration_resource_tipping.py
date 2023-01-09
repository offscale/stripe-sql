from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TerminalConfigurationConfigurationResourceTipping(Base):
    __tablename__ = "terminal_configuration_configuration_resource_tipping"
    aud = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    cad = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    chf = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    czk = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    dkk = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    eur = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    gbp = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    hkd = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    myr = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    nok = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    nzd = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    sek = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    sgd = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    usd = Column(
        Integer,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config.id"
        ),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalConfigurationConfigurationResourceTipping(aud={aud!r}, cad={cad!r}, chf={chf!r}, czk={czk!r}, dkk={dkk!r}, eur={eur!r}, gbp={gbp!r}, hkd={hkd!r}, myr={myr!r}, nok={nok!r}, nzd={nzd!r}, sek={sek!r}, sgd={sgd!r}, usd={usd!r}, id={id!r})".format(
            aud=self.aud,
            cad=self.cad,
            chf=self.chf,
            czk=self.czk,
            dkk=self.dkk,
            eur=self.eur,
            gbp=self.gbp,
            hkd=self.hkd,
            myr=self.myr,
            nok=self.nok,
            nzd=self.nzd,
            sek=self.sek,
            sgd=self.sgd,
            usd=self.usd,
            id=self.id,
        )


__all__ = ["terminal_configuration_configuration_resource_tipping"]
