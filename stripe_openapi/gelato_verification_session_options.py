from sqlalchemy import Column

class Gelato_Verification_Session_Options(Base):
    __tablename__ = 'gelato_verification_session_options'
    document = Column(GelatoSessionDocumentOptions, nullable=True)
    id_number = Column(GelatoSessionIdNumberOptions, nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Gelato_Verification_Session_Options(document={document!r}, id_number={id_number!r})'.format(document=self.document, id_number=self.id_number)
__all__ = ['gelato_verification_session_options']