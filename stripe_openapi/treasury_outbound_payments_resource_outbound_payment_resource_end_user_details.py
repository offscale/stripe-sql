from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails.Json = Table(
    "treasury_outbound_payments_resource_outbound_payment_resource_end_user_details.json",
    metadata,
    Column(
        "ip_address",
        String,
        comment="IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked",
        nullable=True,
    ),
    Column(
        "present",
        Boolean,
        comment="`true`` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "treasury_outbound_payments_resource_outbound_payment_resource_end_user_details.json"
]
