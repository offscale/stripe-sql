from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PortalFeaturesJson = Table(
    "portal_featuresjson",
    metadata,
    Column("customer_update", PortalCustomerUpdate, ForeignKey("PortalCustomerUpdate")),
    Column("invoice_history", PortalInvoiceList, ForeignKey("PortalInvoiceList")),
    Column(
        "payment_method_update",
        PortalPaymentMethodUpdate,
        ForeignKey("PortalPaymentMethodUpdate"),
    ),
    Column(
        "subscription_cancel",
        PortalSubscriptionCancel,
        ForeignKey("PortalSubscriptionCancel"),
    ),
    Column(
        "subscription_pause",
        PortalSubscriptionPause,
        ForeignKey("PortalSubscriptionPause"),
    ),
    Column(
        "subscription_update",
        PortalSubscriptionUpdate,
        ForeignKey("PortalSubscriptionUpdate"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_features.json"]
