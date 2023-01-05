from sqlalchemy import Column, Integer, String


class Subscription_Pending_Invoice_Item_Interval(Base):
    __tablename__ = "subscription_pending_invoice_item_interval"
    interval = Column(
        String,
        comment="Specifies invoicing frequency. Either `day`, `week`, `month` or `year`",
    )
    interval_count = Column(
        Integer,
        comment="The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks)",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Pending_Invoice_Item_Interval(interval={interval!r}, interval_count={interval_count!r}, id={id!r})".format(
            interval=self.interval, interval_count=self.interval_count, id=self.id
        )


__all__ = ["subscription_pending_invoice_item_interval"]
