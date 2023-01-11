from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from . import Base


class Review(Base):
    """
    Reviews can be used to supplement automated fraud detection with human expertise.

    Learn more about [Radar](/radar) and reviewing payments
    [here](https://stripe.com/docs/radar/reviews).

    """

    __tablename__ = "review"
    billing_zip = Column(
        String,
        comment="The ZIP or postal code of the card used, if applicable",
        nullable=True,
    )
    charge = Column(
        Charge,
        ForeignKey("Charge"),
        comment="The charge associated with this review",
        nullable=True,
    )
    closed_reason = Column(
        String,
        comment="The reason the review was closed, or null if it has not yet been closed. One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    ip_address = Column(
        String, comment="The IP address where the payment originated", nullable=True
    )
    ip_address_location = Column(
        Integer,
        ForeignKey("radar_review_resource_location.id"),
        comment="Information related to the location of the payment. Note that this information is an approximation and attempts to locate the nearest population center - it should not be used to determine a specific address",
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
    open = Column(Boolean, comment="If `true`, the review needs action")
    opened_reason = Column(
        String, comment="The reason the review was opened. One of `rule` or `manual`"
    )
    payment_intent = Column(
        String,
        ForeignKey("payment_intent.id"),
        comment="The PaymentIntent ID associated with this review, if one exists",
        nullable=True,
    )
    reason = Column(
        String,
        comment="The reason the review is currently open or closed. One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`, `disputed`, or `redacted`",
    )
    session = Column(
        Integer,
        ForeignKey("radar_review_resource_session.id"),
        comment="Information related to the browsing session of the user who initiated the payment",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Review(billing_zip={billing_zip!r}, charge={charge!r}, closed_reason={closed_reason!r}, created={created!r}, id={id!r}, ip_address={ip_address!r}, ip_address_location={ip_address_location!r}, livemode={livemode!r}, object={object!r}, open={open!r}, opened_reason={opened_reason!r}, payment_intent={payment_intent!r}, reason={reason!r}, session={session!r})".format(
            billing_zip=self.billing_zip,
            charge=self.charge,
            closed_reason=self.closed_reason,
            created=self.created,
            id=self.id,
            ip_address=self.ip_address,
            ip_address_location=self.ip_address_location,
            livemode=self.livemode,
            object=self.object,
            open=self.open,
            opened_reason=self.opened_reason,
            payment_intent=self.payment_intent,
            reason=self.reason,
            session=self.session,
        )


__all__ = ["review"]
