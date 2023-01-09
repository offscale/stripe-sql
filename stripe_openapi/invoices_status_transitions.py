from sqlalchemy import Column, Integer

from . import Base


class InvoicesStatusTransitions(Base):
    __tablename__ = "invoices_status_transitions"
    finalized_at = Column(
        Integer, comment="The time that the invoice draft was finalized", nullable=True
    )
    marked_uncollectible_at = Column(
        Integer,
        comment="The time that the invoice was marked uncollectible",
        nullable=True,
    )
    paid_at = Column(
        Integer,
        comment="The time that the invoice was paid",
        nullable=True,
        primary_key=True,
    )
    voided_at = Column(
        Integer, comment="The time that the invoice was voided", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicesStatusTransitions(finalized_at={finalized_at!r}, marked_uncollectible_at={marked_uncollectible_at!r}, paid_at={paid_at!r}, voided_at={voided_at!r})".format(
            finalized_at=self.finalized_at,
            marked_uncollectible_at=self.marked_uncollectible_at,
            paid_at=self.paid_at,
            voided_at=self.voided_at,
        )


__all__ = ["invoices_status_transitions"]
