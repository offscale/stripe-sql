from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentMethodKlarna(Base):
    __tablename__ = "payment_method_klarna"
    dob = Column(
        Integer,
        ForeignKey("payment_flows_private_payment_methods_klarna_dob.id"),
        comment="The customer's date of birth, if provided",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodKlarna(dob={dob!r}, id={id!r})".format(
            dob=self.dob, id=self.id
        )


__all__ = ["payment_method_klarna"]
