from sqlalchemy import Column, String


class Platform_Tax_Fee(Base):
    __tablename__ = "platform_tax_fee"
    account = Column(String, comment="The Connected account that incurred this charge")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    source_transaction = Column(
        String, comment="The payment object that caused this tax to be inflicted"
    )
    type = Column(String, comment="The type of tax (VAT)")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Platform_Tax_Fee(account={account!r}, id={id!r}, object={object!r}, source_transaction={source_transaction!r}, type={type!r})".format(
            account=self.account,
            id=self.id,
            object=self.object,
            source_transaction=self.source_transaction,
            type=self.type,
        )


__all__ = ["platform_tax_fee"]
