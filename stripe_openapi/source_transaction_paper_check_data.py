from sqlalchemy import Column, Integer, String

class Source_Transaction_Paper_Check_Data(Base):
    __tablename__ = 'source_transaction_paper_check_data'
    available_at = Column(String, comment='Time at which the deposited funds will be available for use. Measured in seconds since the Unix epoch', nullable=True)
    invoices = Column(String, comment='Comma-separated list of invoice IDs associated with the paper check', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Transaction_Paper_Check_Data(available_at={available_at!r}, invoices={invoices!r}, id={id!r})'.format(available_at=self.available_at, invoices=self.invoices, id=self.id)
__all__ = ['source_transaction_paper_check_data']