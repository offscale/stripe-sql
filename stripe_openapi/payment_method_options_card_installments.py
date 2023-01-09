from sqlalchemy import Boolean, Column, Identity, Integer, list

from stripe_openapi.payment_method_details_card_installments_plan import (
    PaymentMethodDetailsCardInstallmentsPlan,
)

from . import Base


class PaymentMethodOptionsCardInstallments(Base):
    __tablename__ = "payment_method_options_card_installments"
    available_plans = Column(
        list,
        comment="Installment plans that may be selected for this PaymentIntent",
        nullable=True,
    )
    enabled = Column(
        Boolean, comment="Whether Installments are enabled for this PaymentIntent"
    )
    plan = Column(
        PaymentMethodDetailsCardInstallmentsPlan,
        comment="[[FK(PaymentMethodDetailsCardInstallmentsPlan)]] Installment plan selected for this PaymentIntent",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodOptionsCardInstallments(available_plans={available_plans!r}, enabled={enabled!r}, plan={plan!r}, id={id!r})".format(
            available_plans=self.available_plans,
            enabled=self.enabled,
            plan=self.plan,
            id=self.id,
        )


__all__ = ["payment_method_options_card_installments"]
