from sqlalchemy import Column, Integer, String

class Source_Type_Eps(Base):
    __tablename__ = 'source_type_eps'
    reference = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Eps(reference={reference!r}, statement_descriptor={statement_descriptor!r}, id={id!r})'.format(reference=self.reference, statement_descriptor=self.statement_descriptor, id=self.id)
__all__ = ['source_type_eps']