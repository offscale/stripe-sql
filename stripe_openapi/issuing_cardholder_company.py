from sqlalchemy import Boolean, Column


class Issuing_Cardholder_Company(Base):
    __tablename__ = "issuing_cardholder_company"
    tax_id_provided = Column(
        Boolean,
        comment="Whether the company's business ID number was provided",
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Cardholder_Company(tax_id_provided={tax_id_provided!r})".format(
            tax_id_provided=self.tax_id_provided
        )


__all__ = ["issuing_cardholder_company"]
