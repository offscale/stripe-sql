from sqlalchemy import Column, ForeignKey, Identity, Integer

from stripe_openapi.quotes_resource_recurring import QuotesResourceRecurring

from . import Base


class QuotesResourceComputed(Base):
    __tablename__ = "quotes_resource_computed"
    recurring = Column(
        QuotesResourceRecurring,
        comment="[[FK(QuotesResourceRecurring)]] The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices",
        nullable=True,
    )
    upfront = Column(Integer, ForeignKey("quotes_resource_upfront.id"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "QuotesResourceComputed(recurring={recurring!r}, upfront={upfront!r}, id={id!r})".format(
            recurring=self.recurring, upfront=self.upfront, id=self.id
        )


__all__ = ["quotes_resource_computed"]
