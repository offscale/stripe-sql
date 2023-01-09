from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class QuotesResourceRecurring(Base):
    __tablename__ = "quotes_resource_recurring"
    amount_subtotal = Column(
        Integer, comment="Total before any discounts or taxes are applied"
    )
    amount_total = Column(
        Integer, comment="Total after discounts and taxes are applied"
    )
    interval = Column(
        String,
        comment="The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`",
    )
    interval_count = Column(
        Integer,
        comment="The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months",
    )
    total_details = Column(Integer, ForeignKey("quotes_resource_total_details.id"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "QuotesResourceRecurring(amount_subtotal={amount_subtotal!r}, amount_total={amount_total!r}, interval={interval!r}, interval_count={interval_count!r}, total_details={total_details!r}, id={id!r})".format(
            amount_subtotal=self.amount_subtotal,
            amount_total=self.amount_total,
            interval=self.interval,
            interval_count=self.interval_count,
            total_details=self.total_details,
            id=self.id,
        )


__all__ = ["quotes_resource_recurring"]
