from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodCardChecks(Base):
    __tablename__ = "payment_method_card_checks"
    address_line1_check = Column(
        String,
        comment="If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    )
    address_postal_code_check = Column(
        String,
        comment="If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    )
    cvc_check = Column(
        String,
        comment="If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodCardChecks(address_line1_check={address_line1_check!r}, address_postal_code_check={address_postal_code_check!r}, cvc_check={cvc_check!r}, id={id!r})".format(
            address_line1_check=self.address_line1_check,
            address_postal_code_check=self.address_postal_code_check,
            cvc_check=self.cvc_check,
            id=self.id,
        )


__all__ = ["payment_method_card_checks"]
