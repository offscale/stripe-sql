from sqlalchemy import Column, Integer, String

class Source_Type_Alipay(Base):
    __tablename__ = 'source_type_alipay'
    data_string = Column(String, nullable=True)
    native_url = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Alipay(data_string={data_string!r}, native_url={native_url!r}, statement_descriptor={statement_descriptor!r}, id={id!r})'.format(data_string=self.data_string, native_url=self.native_url, statement_descriptor=self.statement_descriptor, id=self.id)
__all__ = ['source_type_alipay']