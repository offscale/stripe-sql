from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer

from . import Base


class PaymentFlowsInstallmentOptions(Base):
    __tablename__ = "payment_flows_installment_options"
    enabled = Column(Boolean)
    plan = Column(
        Integer,
        ForeignKey("payment_method_details_card_installments_plan.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentFlowsInstallmentOptions(enabled={enabled!r}, plan={plan!r}, id={id!r})".format(
            enabled=self.enabled, plan=self.plan, id=self.id
        )


__all__ = ["payment_flows_installment_options"]
