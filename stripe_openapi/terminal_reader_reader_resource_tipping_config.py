from sqlalchemy import Column, Integer

class Terminal_Reader_Reader_Resource_Tipping_Config(Base):
    """
    Represents a per-transaction tipping configuration
        """
    __tablename__ = 'terminal_reader_reader_resource_tipping_config'
    amount_eligible = Column(Integer, comment='Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency)', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Terminal_Reader_Reader_Resource_Tipping_Config(amount_eligible={amount_eligible!r}, id={id!r})'.format(amount_eligible=self.amount_eligible, id=self.id)
__all__ = ['terminal_reader_reader_resource_tipping_config']