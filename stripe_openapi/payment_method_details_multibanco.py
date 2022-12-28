from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Multibanco(Base):
    __tablename__ = 'payment_method_details_multibanco'
    entity = Column(String, comment='Entity number associated with this Multibanco payment', nullable=True)
    reference = Column(String, comment='Reference number associated with this Multibanco payment', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Multibanco(entity={entity!r}, reference={reference!r}, id={id!r})'.format(entity=self.entity, reference=self.reference, id=self.id)
__all__ = ['payment_method_details_multibanco']