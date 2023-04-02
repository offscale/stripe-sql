from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentFlowsPrivatePaymentMethodsAlipayDetailsJson = Table(
    "payment_flows_private_payment_methods_alipay_detailsjson",
    metadata,
    Column(
        "buyer_id",
        String,
        comment="Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same",
        nullable=True,
    ),
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same",
        nullable=True,
    ),
    Column(
        "transaction_id",
        String,
        comment="Transaction ID of this particular Alipay transaction",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_private_payment_methods_alipay_details.json"]
