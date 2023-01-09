from sqlalchemy import Column, Integer, String

from . import Base


class TaxDeductedAtSource(Base):
    __tablename__ = "tax_deducted_at_source"
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    period_end = Column(
        Integer,
        comment="The end of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period",
    )
    period_start = Column(
        Integer,
        comment="The start of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period",
    )
    tax_deduction_account_number = Column(
        String, comment="The TAN that was supplied to Stripe when TDS was assessed"
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TaxDeductedAtSource(id={id!r}, object={object!r}, period_end={period_end!r}, period_start={period_start!r}, tax_deduction_account_number={tax_deduction_account_number!r})".format(
            id=self.id,
            object=self.object,
            period_end=self.period_end,
            period_start=self.period_start,
            tax_deduction_account_number=self.tax_deduction_account_number,
        )


__all__ = ["tax_deducted_at_source"]
