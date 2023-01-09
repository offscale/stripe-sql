from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class PortalInvoiceList(Base):
    __tablename__ = "portal_invoice_list"
    enabled = Column(Boolean, comment="Whether the feature is enabled")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalInvoiceList(enabled={enabled!r}, id={id!r})".format(
            enabled=self.enabled, id=self.id
        )


__all__ = ["portal_invoice_list"]
