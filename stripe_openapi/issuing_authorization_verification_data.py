from sqlalchemy import Column, Identity, Integer, String

from . import Base


class IssuingAuthorizationVerificationData(Base):
    __tablename__ = "issuing_authorization_verification_data"
    address_line1_check = Column(
        String,
        comment="Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`",
    )
    address_postal_code_check = Column(
        String,
        comment="Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`",
    )
    cvc_check = Column(
        String,
        comment="Whether the cardholder provided a CVC and if it matched Stripe’s record",
    )
    expiry_check = Column(
        String,
        comment="Whether the cardholder provided an expiry date and if it matched Stripe’s record",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingAuthorizationVerificationData(address_line1_check={address_line1_check!r}, address_postal_code_check={address_postal_code_check!r}, cvc_check={cvc_check!r}, expiry_check={expiry_check!r}, id={id!r})".format(
            address_line1_check=self.address_line1_check,
            address_postal_code_check=self.address_postal_code_check,
            cvc_check=self.cvc_check,
            expiry_check=self.expiry_check,
            id=self.id,
        )


__all__ = ["issuing_authorization_verification_data"]
