from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_method_details_card_installments_plan import (
    PaymentMethodDetailsCardInstallmentsPlan,
)

from . import Base


class PaymentMethodDetailsCardInstallments(Base):
    __tablename__ = "payment_method_details_card_installments"
    plan = Column(
        PaymentMethodDetailsCardInstallmentsPlan,
        comment="[[FK(PaymentMethodDetailsCardInstallmentsPlan)]] Installment plan selected for the payment",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsCardInstallments(plan={plan!r}, id={id!r})".format(
            plan=self.plan, id=self.id
        )


__all__ = ["payment_method_details_card_installments"]
