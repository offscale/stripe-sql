from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class QuotesResourceFromQuote(Base):
    __tablename__ = "quotes_resource_from_quote"
    is_revision = Column(
        Boolean, comment="Whether this quote is a revision of a different quote"
    )
    quote = Column(Quote, comment="[[FK(Quote)]] The quote that was cloned")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "QuotesResourceFromQuote(is_revision={is_revision!r}, quote={quote!r}, id={id!r})".format(
            is_revision=self.is_revision, quote=self.quote, id=self.id
        )


__all__ = ["quotes_resource_from_quote"]
