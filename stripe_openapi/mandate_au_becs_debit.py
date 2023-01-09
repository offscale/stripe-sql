from sqlalchemy import Column, Identity, Integer, String

from . import Base


class MandateAuBecsDebit(Base):
    __tablename__ = "mandate_au_becs_debit"
    url = Column(
        String,
        comment="The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "MandateAuBecsDebit(url={url!r}, id={id!r})".format(
            url=self.url, id=self.id
        )


__all__ = ["mandate_au_becs_debit"]
