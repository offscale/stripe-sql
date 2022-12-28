from sqlalchemy import Column, Integer

class Bank_Connections_Resource_Link_Account_Session_Filters(Base):
    __tablename__ = 'bank_connections_resource_link_account_session_filters'
    countries = Column(ARRAY(String), comment='List of countries from which to filter accounts', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Bank_Connections_Resource_Link_Account_Session_Filters(countries={countries!r}, id={id!r})'.format(countries=self.countries, id=self.id)
__all__ = ['bank_connections_resource_link_account_session_filters']