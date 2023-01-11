from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class SetupIntentPaymentMethodOptionsCard(Base):
    __tablename__ = "setup_intent_payment_method_options_card"
    mandate_options = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options_card_mandate_options.id"),
        comment="Configuration options for setting up an eMandate for cards issued in India",
        nullable=True,
    )
    network = Column(
        String,
        comment="Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the setup intent. Can be only set confirm-time",
        nullable=True,
    )
    request_three_d_secure = Column(
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntentPaymentMethodOptionsCard(mandate_options={mandate_options!r}, network={network!r}, request_three_d_secure={request_three_d_secure!r}, id={id!r})".format(
            mandate_options=self.mandate_options,
            network=self.network,
            request_three_d_secure=self.request_three_d_secure,
            id=self.id,
        )


__all__ = ["setup_intent_payment_method_options_card"]
