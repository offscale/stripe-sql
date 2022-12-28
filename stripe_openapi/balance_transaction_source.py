from sqlalchemy import Column, Integer

class Balance_Transaction_Source(Base):
    __tablename__ = 'balance_transaction_source'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Balance_Transaction_Source(id={id!r})'.format(id=self.id)
__all__ = ['balance_transaction_source']