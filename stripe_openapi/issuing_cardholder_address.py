from sqlalchemy import Column, Integer

class Issuing_Cardholder_Address(Base):
    __tablename__ = 'issuing_cardholder_address'
    address = Column(Address)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Cardholder_Address(address={address!r}, id={id!r})'.format(address=self.address, id=self.id)
__all__ = ['issuing_cardholder_address']