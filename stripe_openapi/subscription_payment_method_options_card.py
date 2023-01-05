from sqlalchemy import Column, Integer, String


class Subscription_Payment_Method_Options_Card(Base):
    __tablename__ = "subscription_payment_method_options_card"
    mandate_options = Column(InvoiceMandateOptionsCard, nullable=True)
    network = Column(
        String,
        comment="Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time",
        nullable=True,
    )
    request_three_d_secure = Column(
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Payment_Method_Options_Card(mandate_options={mandate_options!r}, network={network!r}, request_three_d_secure={request_three_d_secure!r}, id={id!r})".format(
            mandate_options=self.mandate_options,
            network=self.network,
            request_three_d_secure=self.request_three_d_secure,
            id=self.id,
        )


__all__ = ["subscription_payment_method_options_card"]
