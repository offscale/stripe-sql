from sqlalchemy import Column, Integer

class Terminal_Configuration_Configuration_Resource_Tipping(Base):
    __tablename__ = 'terminal_configuration_configuration_resource_tipping'
    aud = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    cad = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    chf = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    czk = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    dkk = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    eur = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    gbp = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    hkd = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    myr = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    nok = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    nzd = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    sek = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    sgd = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    usd = Column(TerminalConfigurationConfigurationResourceCurrencySpecificConfig, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Terminal_Configuration_Configuration_Resource_Tipping(aud={aud!r}, cad={cad!r}, chf={chf!r}, czk={czk!r}, dkk={dkk!r}, eur={eur!r}, gbp={gbp!r}, hkd={hkd!r}, myr={myr!r}, nok={nok!r}, nzd={nzd!r}, sek={sek!r}, sgd={sgd!r}, usd={usd!r}, id={id!r})'.format(aud=self.aud, cad=self.cad, chf=self.chf, czk=self.czk, dkk=self.dkk, eur=self.eur, gbp=self.gbp, hkd=self.hkd, myr=self.myr, nok=self.nok, nzd=self.nzd, sek=self.sek, sgd=self.sgd, usd=self.usd, id=self.id)
__all__ = ['terminal_configuration_configuration_resource_tipping']