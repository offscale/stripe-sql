from sqlalchemy import Column, Identity, Integer, list

from . import Base


class PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown(Base):
    __tablename__ = "payment_pages_checkout_session_total_details_resource_breakdown"
    discounts = Column(list, comment="The aggregated discounts")
    taxes = Column(list, comment="The aggregated tax amounts by rate")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown(discounts={discounts!r}, taxes={taxes!r}, id={id!r})".format(
            discounts=self.discounts, taxes=self.taxes, id=self.id
        )


__all__ = ["payment_pages_checkout_session_total_details_resource_breakdown"]
