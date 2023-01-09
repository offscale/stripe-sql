from sqlalchemy import Boolean, Column, Identity, Integer, String

from . import Base


class AutomaticTax(Base):
    __tablename__ = "automatic_tax"
    enabled = Column(
        Boolean,
        comment="Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices",
    )
    status = Column(
        String,
        comment="The status of the most recent automated tax calculation for this invoice",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AutomaticTax(enabled={enabled!r}, status={status!r}, id={id!r})".format(
            enabled=self.enabled, status=self.status, id=self.id
        )


__all__ = ["automatic_tax"]
