from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentLinksResourceCompletionBehaviorRedirect(Base):
    __tablename__ = "payment_links_resource_completion_behavior_redirect"
    url = Column(
        String,
        comment="The URL the customer will be redirected to after the purchase is complete",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceCompletionBehaviorRedirect(url={url!r}, id={id!r})".format(
            url=self.url, id=self.id
        )


__all__ = ["payment_links_resource_completion_behavior_redirect"]
