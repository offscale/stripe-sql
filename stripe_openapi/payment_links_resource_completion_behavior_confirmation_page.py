from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentLinksResourceCompletionBehaviorConfirmationPage(Base):
    __tablename__ = "payment_links_resource_completion_behavior_confirmation_page"
    custom_message = Column(
        String,
        comment="The custom message that is displayed to the customer after the purchase is complete",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceCompletionBehaviorConfirmationPage(custom_message={custom_message!r}, id={id!r})".format(
            custom_message=self.custom_message, id=self.id
        )


__all__ = ["payment_links_resource_completion_behavior_confirmation_page"]
