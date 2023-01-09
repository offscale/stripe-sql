from sqlalchemy import Boolean, Column, Identity, Integer, String

from . import Base


class QuotesResourceAutomaticTax(Base):
    __tablename__ = "quotes_resource_automatic_tax"
    enabled = Column(Boolean, comment="Automatically calculate taxes")
    status = Column(
        String,
        comment="The status of the most recent automated tax calculation for this quote",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "QuotesResourceAutomaticTax(enabled={enabled!r}, status={status!r}, id={id!r})".format(
            enabled=self.enabled, status=self.status, id=self.id
        )


__all__ = ["quotes_resource_automatic_tax"]
