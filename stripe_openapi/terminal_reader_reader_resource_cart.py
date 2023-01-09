from sqlalchemy import Column, Identity, Integer, String, list

from . import Base


class TerminalReaderReaderResourceCart(Base):
    """
    Represents a cart to be displayed on the reader
    """

    __tablename__ = "terminal_reader_reader_resource_cart"
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    line_items = Column(list, comment="List of line items in the cart")
    tax = Column(
        Integer,
        comment="Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    )
    total = Column(
        Integer,
        comment="Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalReaderReaderResourceCart(currency={currency!r}, line_items={line_items!r}, tax={tax!r}, total={total!r}, id={id!r})".format(
            currency=self.currency,
            line_items=self.line_items,
            tax=self.tax,
            total=self.total,
            id=self.id,
        )


__all__ = ["terminal_reader_reader_resource_cart"]
