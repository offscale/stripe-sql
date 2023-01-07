from sqlalchemy import Column, Integer


class Terminal_Configuration_Configuration_Resource_Tipping(Base):
    __tablename__ = "terminal_configuration_configuration_resource_tipping"
    aud = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    cad = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    chf = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    czk = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    dkk = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    eur = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    gbp = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    hkd = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    myr = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    nok = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    nzd = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    sek = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    sgd = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
        ),
        nullable=True,
    )
    usd = Column(
        terminal_configuration_configuration_resource_currency_specific_config,
        ForeignKey(
            "terminal_configuration_configuration_resource_currency_specific_config"
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
        return "Terminal_Configuration_Configuration_Resource_Tipping(aud={aud!r}, cad={cad!r}, chf={chf!r}, czk={czk!r}, dkk={dkk!r}, eur={eur!r}, gbp={gbp!r}, hkd={hkd!r}, myr={myr!r}, nok={nok!r}, nzd={nzd!r}, sek={sek!r}, sgd={sgd!r}, usd={usd!r}, id={id!r})".format(
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
