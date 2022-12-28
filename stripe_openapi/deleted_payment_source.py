from sqlalchemy import Column, Integer

class Deleted_Payment_Source(Base):
    __tablename__ = 'deleted_payment_source'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Deleted_Payment_Source(id={id!r})'.format(id=self.id)
__all__ = ['deleted_payment_source']