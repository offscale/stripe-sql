from sqlalchemy import Boolean, Column, Integer, String


class Usage_Record_Summary(Base):
    __tablename__ = "usage_record_summary"
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    invoice = Column(
        String,
        comment="The invoice in which this usage period has been billed for",
        nullable=True,
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    period = Column(period, ForeignKey("period"))
    subscription_item = Column(
        String, comment="The ID of the subscription item this summary is describing"
    )
    total_usage = Column(Integer, comment="The total usage within this usage period")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Usage_Record_Summary(id={id!r}, invoice={invoice!r}, livemode={livemode!r}, object={object!r}, period={period!r}, subscription_item={subscription_item!r}, total_usage={total_usage!r})".format(
            id=self.id,
            invoice=self.invoice,
            livemode=self.livemode,
            object=self.object,
            period=self.period,
            subscription_item=self.subscription_item,
            total_usage=self.total_usage,
        )


__all__ = ["usage_record_summary"]
