from sqlalchemy import Column, Integer, String

class Issuing_Card_Shipping_Customs(Base):
    __tablename__ = 'issuing_card_shipping_customs'
    eori_number = Column(String, comment='A registration number used for customs in Europe. See https://www.gov.uk/eori and https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Card_Shipping_Customs(eori_number={eori_number!r}, id={id!r})'.format(eori_number=self.eori_number, id=self.id)
__all__ = ['issuing_card_shipping_customs']