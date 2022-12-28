from sqlalchemy import Column, Integer, String

class Address(Base):
    __tablename__ = 'address'
    city = Column(String, comment='City, district, suburb, town, or village', nullable=True)
    country = Column(String, comment='Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))', nullable=True)
    line1 = Column(String, comment='Address line 1 (e.g., street, PO Box, or company name)', nullable=True)
    line2 = Column(String, comment='Address line 2 (e.g., apartment, suite, unit, or building)', nullable=True)
    postal_code = Column(String, comment='ZIP or postal code', nullable=True)
    state = Column(String, comment='State, county, province, or region', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Address(city={city!r}, country={country!r}, line1={line1!r}, line2={line2!r}, postal_code={postal_code!r}, state={state!r}, id={id!r})'.format(city=self.city, country=self.country, line1=self.line1, line2=self.line2, postal_code=self.postal_code, state=self.state, id=self.id)
__all__ = ['address']