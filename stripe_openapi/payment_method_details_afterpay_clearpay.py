from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodDetailsAfterpayClearpay(Base):
    __tablename__ = "payment_method_details_afterpay_clearpay"
    reference = Column(
        String,
        comment="Order identifier shown to the merchant in Afterpay’s online portal",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsAfterpayClearpay(reference={reference!r}, id={id!r})".format(
            reference=self.reference, id=self.id
        )


__all__ = ["payment_method_details_afterpay_clearpay"]
