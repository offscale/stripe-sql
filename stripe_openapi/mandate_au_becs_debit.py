from sqlalchemy import Column, Integer, String

class Mandate_Au_Becs_Debit(Base):
    __tablename__ = 'mandate_au_becs_debit'
    url = Column(String, comment='The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Mandate_Au_Becs_Debit(url={url!r}, id={id!r})'.format(url=self.url, id=self.id)
__all__ = ['mandate_au_becs_debit']