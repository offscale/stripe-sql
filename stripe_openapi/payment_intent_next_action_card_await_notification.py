from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class PaymentIntentNextActionCardAwaitNotification(Base):
    __tablename__ = "payment_intent_next_action_card_await_notification"
    charge_attempt_at = Column(
        Integer,
        comment="The time that payment will be attempted. If customer approval is required, they need to provide approval before this time",
        nullable=True,
    )
    customer_approval_required = Column(
        Boolean,
        comment="For payments greater than INR 15000, the customer must provide explicit approval of the payment with their bank. For payments of lower amount, no customer action is required",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionCardAwaitNotification(charge_attempt_at={charge_attempt_at!r}, customer_approval_required={customer_approval_required!r}, id={id!r})".format(
            charge_attempt_at=self.charge_attempt_at,
            customer_approval_required=self.customer_approval_required,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_card_await_notification"]
