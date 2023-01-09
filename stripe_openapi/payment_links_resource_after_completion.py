from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class PaymentLinksResourceAfterCompletion(Base):
    __tablename__ = "payment_links_resource_after_completion"
    hosted_confirmation = Column(
        Integer,
        ForeignKey("payment_links_resource_completion_behavior_confirmation_page.id"),
        nullable=True,
    )
    redirect = Column(
        Integer,
        ForeignKey("payment_links_resource_completion_behavior_redirect.id"),
        nullable=True,
    )
    type = Column(
        String, comment="The specified behavior after the purchase is complete"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceAfterCompletion(hosted_confirmation={hosted_confirmation!r}, redirect={redirect!r}, type={type!r}, id={id!r})".format(
            hosted_confirmation=self.hosted_confirmation,
            redirect=self.redirect,
            type=self.type,
            id=self.id,
        )


__all__ = ["payment_links_resource_after_completion"]
