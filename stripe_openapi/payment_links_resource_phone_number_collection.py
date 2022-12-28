from sqlalchemy import Boolean, Column, Integer

class Payment_Links_Resource_Phone_Number_Collection(Base):
    __tablename__ = 'payment_links_resource_phone_number_collection'
    enabled = Column(Boolean, comment='If `true`, a phone number will be collected during checkout')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Links_Resource_Phone_Number_Collection(enabled={enabled!r}, id={id!r})'.format(enabled=self.enabled, id=self.id)
__all__ = ['payment_links_resource_phone_number_collection']