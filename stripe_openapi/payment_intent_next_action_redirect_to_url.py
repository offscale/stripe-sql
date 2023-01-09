from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentNextActionRedirectToUrl(Base):
    __tablename__ = "payment_intent_next_action_redirect_to_url"
    return_url = Column(
        String,
        comment="If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion",
        nullable=True,
    )
    url = Column(
        String,
        comment="The URL you must redirect your customer to in order to authenticate the payment",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionRedirectToUrl(return_url={return_url!r}, url={url!r}, id={id!r})".format(
            return_url=self.return_url, url=self.url, id=self.id
        )


__all__ = ["payment_intent_next_action_redirect_to_url"]
