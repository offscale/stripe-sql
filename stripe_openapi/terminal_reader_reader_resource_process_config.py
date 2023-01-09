from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer

from . import Base


class TerminalReaderReaderResourceProcessConfig(Base):
    """
    Represents a per-transaction override of a reader configuration
    """

    __tablename__ = "terminal_reader_reader_resource_process_config"
    skip_tipping = Column(
        Boolean,
        comment="Override showing a tipping selection screen on this transaction",
        nullable=True,
    )
    tipping = Column(
        Integer,
        ForeignKey("terminal_reader_reader_resource_tipping_config.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalReaderReaderResourceProcessConfig(skip_tipping={skip_tipping!r}, tipping={tipping!r}, id={id!r})".format(
            skip_tipping=self.skip_tipping, tipping=self.tipping, id=self.id
        )


__all__ = ["terminal_reader_reader_resource_process_config"]
