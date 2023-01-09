from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class OutboundTransfersPaymentMethodDetails(Base):
    __tablename__ = "outbound_transfers_payment_method_details"
    billing_details = Column(
        Integer, ForeignKey("treasury_shared_resource_billing_details.id")
    )
    type = Column(
        String, comment="The type of the payment method used in the OutboundTransfer"
    )
    us_bank_account = Column(
        String,
        ForeignKey(
            "outbound_transfers_payment_method_details_us_bank_account.bank_name"
        ),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "OutboundTransfersPaymentMethodDetails(billing_details={billing_details!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})".format(
            billing_details=self.billing_details,
            type=self.type,
            us_bank_account=self.us_bank_account,
            id=self.id,
        )


__all__ = ["outbound_transfers_payment_method_details"]
