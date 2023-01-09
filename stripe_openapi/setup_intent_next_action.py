from sqlalchemy import JSON, Column, ForeignKey, Identity, Integer, String

from . import Base


class SetupIntentNextAction(Base):
    __tablename__ = "setup_intent_next_action"
    redirect_to_url = Column(
        Integer,
        ForeignKey("setup_intent_next_action_redirect_to_url.id"),
        nullable=True,
    )
    type = Column(
        String,
        comment="Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`",
    )
    use_stripe_sdk = Column(
        JSON,
        comment="When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js",
        nullable=True,
    )
    verify_with_microdeposits = Column(
        Integer,
        ForeignKey("setup_intent_next_action_verify_with_microdeposits.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentNextAction(redirect_to_url={redirect_to_url!r}, type={type!r}, use_stripe_sdk={use_stripe_sdk!r}, verify_with_microdeposits={verify_with_microdeposits!r}, id={id!r})".format(
            redirect_to_url=self.redirect_to_url,
            type=self.type,
            use_stripe_sdk=self.use_stripe_sdk,
            verify_with_microdeposits=self.verify_with_microdeposits,
            id=self.id,
        )


__all__ = ["setup_intent_next_action"]
