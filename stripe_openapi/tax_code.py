from sqlalchemy import Column, String


class Tax_Code(Base):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    __tablename__ = "tax_code"
    description = Column(
        String,
        comment="A detailed description of which types of products the tax code represents",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    name = Column(String, comment="A short name for the tax code")
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
        return "Tax_Code(description={description!r}, id={id!r}, name={name!r}, object={object!r})".format(
            description=self.description, id=self.id, name=self.name, object=self.object
        )


__all__ = ["tax_code"]
