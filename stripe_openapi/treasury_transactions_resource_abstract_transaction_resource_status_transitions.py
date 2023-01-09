from sqlalchemy import Column, Integer

from . import Base


class TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions(Base):
    __tablename__ = "treasury_transactions_resource_abstract_transaction_resource_status_transitions"
    posted_at = Column(
        Integer,
        comment="Timestamp describing when the Transaction changed status to `posted`",
        nullable=True,
    )
    void_at = Column(
        Integer,
        comment="Timestamp describing when the Transaction changed status to `void`",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions(posted_at={posted_at!r}, void_at={void_at!r})".format(
            posted_at=self.posted_at, void_at=self.void_at
        )


__all__ = [
    "treasury_transactions_resource_abstract_transaction_resource_status_transitions"
]
