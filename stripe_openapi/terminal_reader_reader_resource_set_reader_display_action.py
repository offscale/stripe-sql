from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.terminal_reader_reader_resource_cart import (
    TerminalReaderReaderResourceCart,
)

from . import Base


class TerminalReaderReaderResourceSetReaderDisplayAction(Base):
    """
    Represents a reader action to set the reader display
    """

    __tablename__ = "terminal_reader_reader_resource_set_reader_display_action"
    cart = Column(
        TerminalReaderReaderResourceCart,
        comment="[[FK(TerminalReaderReaderResourceCart)]] Cart object to be displayed by the reader",
        nullable=True,
    )
    type = Column(String, comment="Type of information to be displayed by the reader")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalReaderReaderResourceSetReaderDisplayAction(cart={cart!r}, type={type!r}, id={id!r})".format(
            cart=self.cart, type=self.type, id=self.id
        )


__all__ = ["terminal_reader_reader_resource_set_reader_display_action"]
