from sqlalchemy import Boolean, Column, String

from . import Base


class DeletedBankAccount(Base):
    __tablename__ = "deleted_bank_account"
    currency = Column(
        String,
        comment="Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account",
        nullable=True,
    )
    deleted = Column(Boolean, comment="Always true for a deleted object")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "DeletedBankAccount(currency={currency!r}, deleted={deleted!r}, id={id!r}, object={object!r})".format(
            currency=self.currency, deleted=self.deleted, id=self.id, object=self.object
        )


__all__ = ["deleted_bank_account"]
