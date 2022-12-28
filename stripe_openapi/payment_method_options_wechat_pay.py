from sqlalchemy import Column, String

class Payment_Method_Options_Wechat_Pay(Base):
    __tablename__ = 'payment_method_options_wechat_pay'
    app_id = Column(String, comment='The app ID registered with WeChat Pay. Only required when client is ios or android', nullable=True, primary_key=True)
    client = Column(String, comment='The client type that the end customer will pay from', nullable=True)
    setup_future_usage = Column(String, comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)", nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Options_Wechat_Pay(app_id={app_id!r}, client={client!r}, setup_future_usage={setup_future_usage!r})'.format(app_id=self.app_id, client=self.client, setup_future_usage=self.setup_future_usage)
__all__ = ['payment_method_options_wechat_pay']