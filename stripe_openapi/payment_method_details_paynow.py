from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodDetailsPaynow(Base):
    __tablename__ = "payment_method_details_paynow"
    reference = Column(
        String,
        comment="Reference number associated with this PayNow payment",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsPaynow(reference={reference!r}, id={id!r})".format(
            reference=self.reference, id=self.id
        )


__all__ = ["payment_method_details_paynow"]
