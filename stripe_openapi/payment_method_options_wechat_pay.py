from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodOptionsWechatPayJson = Table(
    "payment_method_options_wechat_payjson",
    metadata,
    Column(
        "app_id",
        String,
        comment="The app ID registered with WeChat Pay. Only required when client is ios or android",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "client",
        String,
        comment="The client type that the end customer will pay from",
        nullable=True,
    ),
    Column(
        "setup_future_usage",
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    ),
)
__all__ = ["payment_method_options_wechat_pay.json"]
