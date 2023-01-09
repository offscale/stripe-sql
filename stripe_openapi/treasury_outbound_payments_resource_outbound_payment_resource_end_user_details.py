from sqlalchemy import Boolean, Column, Identity, Integer, String

from . import Base


class TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails(Base):
    __tablename__ = (
        "treasury_outbound_payments_resource_outbound_payment_resource_end_user_details"
    )
    ip_address = Column(
        String,
        comment="IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked",
        nullable=True,
    )
    present = Column(
        Boolean,
        comment="`true`` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails(ip_address={ip_address!r}, present={present!r}, id={id!r})".format(
            ip_address=self.ip_address, present=self.present, id=self.id
        )


__all__ = [
    "treasury_outbound_payments_resource_outbound_payment_resource_end_user_details"
]
