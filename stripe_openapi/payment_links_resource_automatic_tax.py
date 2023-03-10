from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class PaymentLinksResourceAutomaticTax(Base):
    __tablename__ = "payment_links_resource_automatic_tax"
    enabled = Column(
        Boolean,
        comment="If `true`, tax will be calculated automatically using the customer's location",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "PaymentLinksResourceAutomaticTax(enabled={enabled!r}, id={id!r})".format(
                enabled=self.enabled, id=self.id
            )
        )


__all__ = ["payment_links_resource_automatic_tax"]
