from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class CheckoutCardInstallmentsOptions(Base):
    __tablename__ = "checkout_card_installments_options"
    enabled = Column(
        Boolean, comment="Indicates if installments are enabled", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CheckoutCardInstallmentsOptions(enabled={enabled!r}, id={id!r})".format(
            enabled=self.enabled, id=self.id
        )


__all__ = ["checkout_card_installments_options"]
